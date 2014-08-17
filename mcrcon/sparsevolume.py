#!/usr/bin/env python
#
# File: $Id$
#
"""
For some operations we want to locally store and represent a cuboid
shaped volume of blocks.

We want to store this space efficiently but in a structure that is
relatively simple to understand and manipulate.

The simple idea is that in minecraft, in most given volumes that will be
manipulated there is one type of block that is the majority of the volume.

For this block type we do not store it in our sparse volume. Any attempt to
retrieve a block at coordinates that results in nothing is pointing at a
coordinate that has what we have determined as the most common block in
this volume.

Otherwise we find a block at a certain set of coordinates.

Generally the volumes we are dealing with are small, let us say 256x256x256
at most (if that even).

We also want to have the sparse volume be filled on the fly - which means
that as we set blocks in a sparse volume the block that is the 'most
common' is likely to change.

In this case we will just re-write the sparse volume to represent that fact.

The worse case scenario is one where every possible block type is used
equally and we have to just pick one as 'the most common'.

Users of the sparse block do not have to worry about this and just access
the blocks they want through the coordinate system.

XXX This is really just an experimental hack. The way we store keys and
    such is NOT time efficient, really.

    There are definitely better ways to do this. However they tend to be
    very heavy weight and not nearly as obvious how data is stored.. and
    they are also designed for volumes much bigger than this. I suspect
    that there will be serious issues getting more than a couple thousand
    blocks at once over the rcon protocol anyways.

    Really I just wanthing something that was very small and self
    contained and not as naieve as just storing every element in the
    cuboid.

XXX Right now the sparsevolume depends too much on knowing the internals of
    the blocks. Need to go through and pull out that should be in block.py
    instead of sparsevolume.py
"""

# system imports
#
from collections import defaultdict
import copy
import json

# our imports
#
import block


########################################################################
########################################################################
#
class SparseVolume(object):
    """
    The SparseVolume class. It is intended to be a slightly more efficient
    way of storing a volume of minecraft blocks where frequently one block
    type is the most commonly occuring in that volume.

    It is not fast (using a dict plus some logic for setting and getting)
    but it is a lot more straight forward to both implement and use than
    more complex octree or other such branch structures.

    For our use case (copying and examining smallish subsets of a minecraft
    world) it is fast enough, and it is a lot more space efficient than a 3
    dimensional array would be.

    The basic idea is simple: We use a dict whose keys are a tuple of
    (x,y,z) coordinates. For the value we store a reference to one of the
    defined blocks from the blocks module.

    The twist is that: we do NOT store the most common block in this
    dict. If we look up an (x,y,z) coordinate and it is NOT in the
    dictioinary, then its block type is that of the most commonly occuring
    block in that volume.

    When manipulating the SparseVolume whenever you set a coordinate to a
    block, if that causes an element to be inserted in to the dict, this
    means that you have just reduced the count of the currently most common
    block type by 1. If the current mcb (most common block) is no longer
    the most common block after that we basically create a new dict where
    the new mcb is the mcb.. and we then replace our dict with this new
    one.

    This means that we also keep a dict which has the count of the various
    block types that exist in the SparseVolume.

    Two SparseVolumes are the same if their dicts are the same (ie: the
    same block types at the same coordinates in the volume.)

    I have done no real analysis on the speed or efficiency outside of some
    simple comparisons of samples of a minecraft world.
    """

    ####################################################################
    #
    def __init__(self, width, height, depth, hint=block.AIR,
                 rejigger=True):
        """

        hint - a suggestion of what to use as the initial 'most common block'
        """
        self.width = width    # x
        self.height = height  # y
        self.depth = depth    # z
        self.size = self.width * self.height * self.depth
        self.clear(hint)
        self.do_rejigger = rejigger
        return

    ####################################################################
    #
    def get(self, coords):
        """
        NOTE: Coords must be all ints.. maybe we should only use vec3 points.
        """
        if coords in self.v:
            return self.v[coords]
        else:
            return self.mcb

    ####################################################################
    #
    def set(self, coords, block):
        """
        Set a block.. in addition to setting the block in our dict we track the
        counts of the blocks we have set and potentitally re-jigger what
        block is considered the 'mcb'

        NOTE: of course, we really need to revisit how often we consider
              re-jiggering the entire sparse volume.. if we have a race
              between two (or more) blocks for the most common block we
              will be spending painful amounts of time re-jiggering the
              sparse volume.

              Maybe re-jigger should be a call tha the user can make when
              they believe they know when it is best to compute it.
        """
        dst_block = self.get(coords)
        if dst_block == block:
            return

        self.block_counts[dst_block] -= 1
        self.block_counts[block] += 1

        if coords in self.v:
            if block is self.mcb:
                del self.v[coords]
            else:
                self.v[coords] = block
        else:
            # We only get here if the block being set WAS the mcb and now
            # it is something else. Thus we do a rejigger check after we
            # set the block.
            #
            self.v[coords] = block
            self.rejigger()

        return

    ####################################################################
    #
    def to_json(self):
        """
        Dump out what we need to represent a SparseVolume to json
        """
        # We always force a re-jigger before we dump
        #
        self.rejigger(force=True)
        return json.dumps(
            {
                'width': self.width,
                'height': self.height,
                'depth': self.depth,
                'mcb': (self.mcb.id, self.mcb.data),
                'v': {','.join(str(i) for i in k): (v.id, v.data)
                      for k, v in self.v.iteritems()}
            }
        )

    ####################################################################
    #
    @classmethod
    def from_json(cls, json_data):
        """
        Keyword Arguments:
        json_data --
        """
        data = json.loads(json_data)
        mcb = block.Block.lookup(*data['mcb'])
        sv = cls(data['width'], data['height'], data['depth'], hint=mcb,
                 rejigger=False)
        for k, v in data['v'].iteritems():
            sv.set(tuple((int(i) for i in k.split(','))),
                   block.Block.lookup(*v))

        # Now that we are done populating the sparse volume dict we can let
        # rejiggers happen normally.
        #
        sv.do_rejigger = True

        # This should be a noop but just incase the json data was not
        # properly jiggered
        #
        sv.rejigger(force=True)
        return sv

    ####################################################################
    #
    def __copy__(self):
        sv = SparseVolume(self.width, self.height, self.depth, hint=self.mcb,
                          rejigger=False)
        sv.block_counts = copy.copy(self.block_counts)
        sv.v = copy.copy(self.v)

        # Now that we are done populating the sparse volume dict we can let
        # rejiggers happen normally.
        #
        sv.do_rejigger = True

        # This should be a noop but just incase the json data was not
        # properly jiggered
        #
        sv.rejigger(force=True)
        return sv

    ####################################################################
    #
    def clone(self):
        return self.__copy__()

    ####################################################################
    #
    def __eq__(self, rhs):
        """
        equal if the dicts are equal.. to insure this we force a rejigger
        before comparison.

        Keyword Arguments:
        rhs --
        """
        self.rejigger(force=True)
        rhs.rejigger(force=True)
        return self.v == rhs.v

    ####################################################################
    #
    def __ne__(self, rhs):
        return not self.__eq__(rhs)

    ####################################################################
    #
    def __repr__(self):
        return (
            "SparseVolume(width=%d, height=%d, depth=%d, mcb=%s, "
            "blocks=%s" % (self.width, self.height, self.depth,
                           self.mcb, self.v))

    ####################################################################
    #
    def clear(self, block=None):
        """
        Set all blocks to the most common block (or the provided block.. which
        becomes the new most common block.)

        Keyword Arguments:
        block -- (default None)
        """
        self.v = {}
        if block is not None:
            self.mcb = block
        self.block_counts = defaultdict(int)
        self.block_counts[self.mcb] = self.size

    ####################################################################
    #
    def rejigger(self, force=False):
        """
        check the block counts to see if the current mcb is still the actual
        mcb.

        Keyword Arguments:
        force -- (default True)
        """
        if self.do_rejigger is False and force is False:
            return

        if len(self.v) == 0:
            return

        # Find the most common block.
        #
        new_mcb = max(self.block_counts.items(), key=lambda x: x[1])[0]

        # If the actual most common block is not the currently set most
        # common block then create a new v dict that re-jiggers everythign
        # where the new mcb is the one for points in the dict that is not
        # set
        #
        if new_mcb == self.mcb:
            return

        new_v = {}

        # Copy all of the set items in the existing v that are not the
        # new_mcb.
        #
        for k, v in self.v.items():
            if v != new_mcb:
                new_v[k] = v

        # Now go through the entire range of our volume. If these
        # coordinates exist in the new volume dict, then skip that
        # point.. it has already been copied. However, if that
        # coordinate is NOT in the old volume, then that means that at
        # that coordinate was the former mcb, which is no longer the
        # mcb so it needs to be set in the new volume dict.
        #
        for x in range(self.width):
            for y in range(self.height):
                for z in range(self.depth):
                    if (x, y, z) in new_v:
                        next
                    if (x, y, z) not in self.v:
                        new_v[(x, y, z)] = self.mcb

        # And now we have rejiggered our volume.
        #
        self.v = new_v
        self.mcb = new_mcb

        return


#############################################################################
#
def test():
    """
    a simple set of tests

    XXX Skipping a test harness because most of the tricky stuff involves
        talking to a minecraft server.. however making sure sparse volumes
        work right is important and self contained.
    """
    sv = SparseVolume(5, 5, 5)
    assert(sv.size == 125)
    assert(sv.block_counts[block.AIR] == 125)
    sv.set((0, 0, 0), block.STONE)
    assert(sv.block_counts[block.AIR] == 124)
    assert(sv.block_counts[block.STONE] == 1)
    assert(sv.get((0, 0, 0)) is block.STONE)
    for x in range(5):
        for y in range(5):
            for z in range(5):
                if (x, y, z) == (0, 0, 0):
                    assert(sv.get((x, y, z)) is block.STONE)
                else:
                    assert(sv.get((x, y, z)) is block.AIR)

    # Now start filling up the sparse volume with STONE. When the counts
    # for number of stone is greater than that for air the sparse volume
    # should be rejiggered.
    #
    for x in range(5):
        for y in range(3):
            for z in range(5):
                sv.set((x, y, z), block.STONE)

    assert(sv.block_counts[block.AIR] == 50)
    assert(sv.block_counts[block.STONE] == 75)
    assert(sv.mcb is block.STONE)

    for x in range(5):
        for y in range(3):
            for z in range(5):
                assert(sv.get((x, y, z)) is block.STONE)

    for x in range(5):
        for y in range(4, 5):
            for z in range(5):
                assert(sv.get((x, y, z)) is block.AIR)

    # Test our to and from json..
    #
    json_data = sv.to_json()
    new_sv = SparseVolume.from_json(json_data)

    # and make sure our new sv has blocks in the right place
    #
    for x in range(5):
        for y in range(3):
            for z in range(5):
                assert(new_sv.get((x, y, z)) is block.STONE)

    for x in range(5):
        for y in range(4, 5):
            for z in range(5):
                assert(new_sv.get((x, y, z)) is block.AIR)

    # And now make sure our eq & ne operators work.
    #
    assert(sv == new_sv)

    # Set a block so they are different
    #
    new_sv.set((1, 1, 1), block.COBBLESTONE)
    assert(sv != new_sv)

    # and make sure that our clone/copy operation does the right thing..
    #
    clone_sv = sv.clone()
    assert(sv == clone_sv)
    # Set a block so they are different
    #
    clone_sv.set((1, 1, 1), block.COBBLESTONE)
    assert(sv != clone_sv)

    # and make sure the 'copy' module does the right thing too.
    #
    copy_sv = sv.clone()
    assert(sv == copy_sv)
    # Set a block so they are different
    #
    copy_sv.set((1, 1, 1), block.COBBLESTONE)
    assert(sv != copy_sv)

    return

############################################################################
############################################################################
#
# Here is where it all starts
#
if __name__ == '__main__':
    test()
#
############################################################################
############################################################################
