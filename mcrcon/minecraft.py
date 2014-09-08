#!/usr/bin/env python
#
# File: $Id$
#
"""
Our API for manipulating the minecraft server through rcon. We
expose the commands that minecraft supports over rcon as methods on a
class.

List of commands and explanations gleaned and copied from:
http://minecraft.gamepedia.com/Commands

"""

# system imports
#
import math
import re
import json

# 3rd party imports
#

# our module imports
#
import mcrcon
import block
from util import flatten
from sparsevolume import SparseVolume

SURVIVAL = 'survival'
CREATIVE = 'creative'
ADVENTURE = 'adventure'

SCOREBOARD_PLAYERS = 'players'
SCOREBOARD_OBJECTIVES = 'objectives'
SCOREBOARD_TEAMS = 'teams'

BLOCK_DESTROY = "destroy"
BLOCK_HOLLOW = "hollow"
BLOCK_KEEP = "keep"
BLOCK_OUTLINE = "outline"
BLOCK_REPLACE = "replace"


####################################################################
#
def int_floor(*args):
    return [int(math.floor(x)) for x in flatten(args)]


####################################################################
#
def c_range(i, j):
    """
    Range the two values so we produce an inclusive range().
    Automatically deal with i > j by stepping backwards. This
    lets people decide if they want to build bottom up or top
    down, etc.
    """
    i = int(i)
    j = int(j)
    if i > j:
        for k in range(i, j-1, -1):
            yield k
    else:
        for k in range(i, j+1):
            yield k


########################################################################
########################################################################
#
class MCException(Exception):
    def __init__(self, msg):
        super(MCException, self).__init__(msg)


########################################################################
########################################################################
#
class OutsideLoadedWorld(MCException):
    def __init__(self, msg):
        super(OutsideLoadedWorld, self).__init__(
            "Block outside of the loaded world: " + msg
        )


########################################################################
########################################################################
#
class PlayerCannotBeFound(MCException):
    def __init__(self, msg):
        super(PlayerCannotBeFound, self).__init__(
            "Player cannot be found: " + msg
        )


########################################################################
########################################################################
#
class UnhandledResponse(MCException):
    def __init__(self, msg):
        super(UnhandledResponse, self).__init__(
            "Unexpected response from minecraft server: " + msg
        )


########################################################################
########################################################################
#
class UnknownBlock(MCException):
    def __init__(self, msg):
        super(UnknownBlock, self).__init__(
            "Unknown block: " + msg
        )


########################################################################
########################################################################
#
class Minecraft(object):
    """
    API interface to minecraft server via rcon
    """

    # Regexps used in matching responses from the server
    #
    FOUND_BLOCK = re.compile("-?\d+ is ([^(]+) \(", re.IGNORECASE)
    TESTED_DATA = re.compile("had the data value of (\d+)", re.IGNORECASE)

    ####################################################################
    #
    def __init__(self, connection):
        self.conn = connection
        return

    ####################################################################
    #
    @classmethod
    def create(cls, password, address="localhost", port=25575):
        """
        Keyword Arguments:
        cls      -- class method... `Minecraft`
        password -- password... we make it required, as it should be
        address  -- (default "localhost")
        port     -- (default 25575)
        """
        return cls(mcrcon.MCRcon(address, port, password))

    ####################################################################
    #
    def set_achievement(self, achievement, player):
        """
        Keyword Arguments:
        achievment --
        player     --
        """
        res = self.conn.send("achievement give %s %s" %
                             (achievement.command_output, player))
        if res == "That player cannot be found":
            raise PlayerCannotBeFound(player)
        return res

    ####################################################################
    #
    def ban_player(self, player, reason=None):
        """
        These commands manage a server banlist. The server banlist is a
        list of players or IP addresses that will not be allowed to
        connect to the server. Bans supersede any whitelisting in
        place.

        Keyword Arguments:
        player --
        """
        if reason:
            res = self.conn.send("ban %s" % player)
        else:
            res = self.conn.send("ban %s %s" % (player, reason))

        if res[0:21] == "Could not ban player ":
            raise PlayerCannotBeFound(res)

        return res

    ####################################################################
    #
    def ban_ip(self, address, reason):
        """
        Adds IP address to banlist. The address can be a player name or an
        IP address (if it is a player it bans the IP that the player
        is connecting from)

        Keyword Arguments:
        ip_address --
        """
        if reason:
            res = self.conn.send("ban %s" % address)
        else:
            res = self.conn.send("ban %s %s" % (address, reason))

        if res == "You have entered an invalid IP address or a player " \
                  "that is not online":
            raise ValueError(res)

        return res

    ####################################################################
    #
    def list_bans(self):
        """
        returns a tuple of player bans and ip bans
        """
        pass

    ####################################################################
    #
    def clear(self, player, item=None, data=None):
        """
        Clears items from player inventory.

        If the item's 'data' is 0
        Keyword Arguments:
        player --
        item   -- (default None)
        data   -- (default None)
        """
        if item is None:
            res = self.conn.send("clear %s" % player)
        elif data is None:
            res = self.conn.send("clear %s %s" % (player,
                                                  item.command_output))
        else:
            res = self.conn.send("clear %s %s" % (player,
                                                  item.id,
                                                  data.command_output))

        if res == "That player cannot be found":
            raise PlayerCannotBeFound(player)

        return res

    ####################################################################
    #
    def debug(self, enable):
        """
        Keyword Arguments:
        enable --
        """
        return

    ####################################################################
    #
    def set_default_game_mode(self, mode=SURVIVAL):
        """
        Keyword Arguments:
        mode -- (default SURVIVAL)
        """
        return

    ####################################################################
    #
    def deop(self, player):
        """
        Keyword Arguments:
        player --
        """
        return

    ####################################################################
    #
    def set_game_difficulity(self, difficulty_level):
        """
        Keyword Arguments:
        difficulty_level --
        """
        return

    ####################################################################
    #
    def set_effect_on_player(self, player, effect, seconds=10, amplifier=1):
        """
        Keyword Arguments:
        player    --
        effect    --
        seconds   -- (default 10)
        amplifier -- (default 1)
        """
        return

    ####################################################################
    #
    def set_game_mode(self, mode=SURVIVAL, player=None):
        """
        Keyword Arguments:
        mode   -- (default SURVIVAL)
        player -- (default None)
        """
        return

    ####################################################################
    #
    def set_game_rule(self, rule_name, value=None):
        """
        Keyword Arguments:
        rule_name --
        value     -- (default None)
        """
        return

    ####################################################################
    #
    def give_player_item(self, player, item, amount=1, data_tag=None):
        """
        Keyword Arguments:
        player   --
        item     --
        amount   -- (default 1)
        data_tag -- Specifies the data tag of the given
                    item(s). Must be a compound NBT tag (for example,
                    {display:{Name:Fred}}).
        """
        if data_tag is None:
            res = self.conn.send("give %s %s %d %s" % (player, item.id, amount,
                                                       item.data))
        else:
            res = self.conn.send("give %s %s %d %s %s" % (player, item.id,
                                                          amount, item.data,
                                                          json.dumps(data_tag)
                                                          ))
        return res

    ####################################################################
    #
    def kick_player(self, player, reason=None):
        """
        Keyword Arguments:
        player  --
        reason -- (default None)
        """
        if reason is not None:
            res = self.conn.send("kick %s %s" % (player, reason))
        else:
            res = self.conn.send("kick %s" % player)
        return res

    ####################################################################
    #
    def kill(self, player_entity):
        res = self.conn.send("kill %s" % player_entity)
        return res

    ####################################################################
    #
    def list_players(self):
        """

        """
        return

    ####################################################################
    #
    def op_player(self, player):
        """
        Keyword Arguments:
        player --
        """
        res = self.conn.send("op %s" % player)
        return res

    ####################################################################
    #
    def pardon_player(self, player):
        """
        Keyword Arguments:
        player --
        """
        res = self.conn.send("pardon %s" % player)
        return res

    ####################################################################
    #
    def pardon_ip(self, ip_address):
        """
        Keyword Arguments:
        ip_address --
        """
        res = self.conn.send("pardon %s" % ip_address)
        return res

    ####################################################################
    #
    def play_sound(self, sound, player, vec=None, pitch=None, min_vol=None):
        """
        Keyword Arguments:
        sound   --
        player  --
        vec     -- (default None)
        pitch   -- (default None)
        min_vol -- (default None)
        """
        if min_vol is None:
            res = self.conn.send("playsound %s %s %s %s %s %f %f" %
                                 sound.command_output, player, vec[0], vec[1],
                                 vec[2], pitch)
        else:
            res = self.conn.send("playsound %s %s %s %s %s %f %f %f" %
                                 sound.command_output, player, vec[0], vec[1],
                                 vec[2], pitch, min_vol)
        return res

    ####################################################################
    #
    def checkpoint(self):
        """

        """
        return

    ####################################################################
    #
    def auto_save_off(self):
        """

        """
        return

    ####################################################################
    #
    def auto_save_on(self):
        """

        """
        return

    ####################################################################
    #
    def say(self, message):
        """
        Keyword Arguments:
        message --
        """
        self.conn.send("say %s" % message)
        return

    ####################################################################
    #
    def scoreboard(self, cls=SCOREBOARD_PLAYERS):
        """
        Keyword Arguments:
        cls -- (default PLAYERS)
        """
        return

    ####################################################################
    #
    def seed(self):
        """

        """
        return

    ####################################################################
    #
    def set_block(self, coords, block, old_block_handling=BLOCK_REPLACE):
        """
        Keyword Arguments:
        coords             --
        block              --

        old_block_handling -- (default "replace") Specifies how to handle the
                              block change. Must be one of:

                              destroy - The old block drops both itself and
                                         its contents (as if destroyed by a
                                         player). Plays the appropriate block
                                         breaking noise.
                              keep - Only air blocks will be changed
                                      (non-air blocks will be "kept").
                              replace - The old block drops neither itself
                                         nor any contents. Plays no sound.
        """
        coords = int_floor(coords)
        res = self.conn.send("setblock %d %d %d %s" % (coords[0],
                                                       coords[1],
                                                       coords[2],
                                                       block.command_output))
        if res == "Cannot place block outside of the world":
            raise OutsideLoadedWorld(
                "%s at (%d,%d,%d)" % (block, coords[0], coords[1], coords[2])
            )
        if res not in ("Block placed", "The block couldn't be placed"):
            raise UnhandledResponse(res)

        return res

    ####################################################################
    #
    def fill(self, coords0, coords1, block, old_block_handling=BLOCK_REPLACE,
             data_tag=None, replacement_block=None, relative=False):
        """
        Keyword Arguments:
        coords0            --
        coords1            --
        block              --
        old_block_handling -- (default REPLACE)
        data_tag           -- (default None)
        replacement_block  -- (default None)
        relative           -- (default False) If specified than the second set
                              of coords are not an absolute x,y,z
                              position, but are instead width(x),
                              height(y), depth(z) and must be positive,
                              non-zero values
        """
        if old_block_handling is not BLOCK_REPLACE and \
           replacement_block is not None:
            raise ValueError("Can not specify replacement_block (%s) if "
                             "old_block_handling is not 'REPLACE' (%s)" %
                             (old_block_handling, replacement_block))

        if data_tag is not None and replacement_block is not None:
            raise ValueError("Can not specify both data_tag (%s) and "
                             "replacement_block (%s)" %
                             (data_tag, replacement_block))

        x0, y0, z0 = int_floor(coords0)
        x1, y1, z1 = int_floor(coords1)
        if relative:
            if x1 < 1 or y1 < 1 or z1 < 1:
                raise ValueError("Realtive coordinates must be positive, "
                                 "non-zero integers, not: (%s, %s, %s)" %
                                 (x1, y1, z1))
            x1 += x0
            y1 += y0
            z1 += z0

        msg = "fill %d %d %d %d %d %d %s %s" % (x0, y0, z0,
                                                x1, y1, z1,
                                                block.command_output,
                                                old_block_handling)
        if data_tag is not None:
            msg += data_tag
        if replacement_block is not None:
            msg += replacement_block.command_output

        print "Sending message: '%s'" % msg
        res = self.conn.send(msg)
        return res

    ####################################################################
    #
    def set_blocks_from_sparsevolume(self, coords, sv,
                                     old_block_handling="replace"):
        """
        Given a SparseVolume set blocks according to its content, where the
        sparse volume will be rooted at the given coordinates.

        The new blocks will be filled y layer at a time moving up. This
        is so that gravity affected blocks like sand and gravel in the
        SparseVolume are laid out correctly.

        Keyword Arguments:
        coords --
        sv     --
        """
        x, y, z = coords
        for iy in range(sv.height):
            for ix in range(sv.width):
                for iz in range(sv.depth):
                    self.set_block((x+ix, y+iy, z+iz), sv.get((ix, iy, iz)),
                                   old_block_handling=old_block_handling)
        return

    ####################################################################
    #
    def set_idle_timeout(self, minutes=0):
        """
        Keyword Arguments:
        minutes -- (default 0)
        """
        return

    ####################################################################
    #
    def set_world_spawn_point(self, coords):
        """
        Keyword Arguments:
        coords --
        """
        return

    ####################################################################
    #
    def set_player_spawn_point(self, coords):
        """
        Keyword Arguments:
        coords --
        """
        return

    ####################################################################
    #
    def spread_players(self, coords, spread_distance, max_range,
                       respect_teams=True, players=None):
        """
        Keyword Arguments:
        coords          --
        spread_distance --
        max_range       --
        respect_teams   -- (default True)
        players         -- (default None)
        """
        return

    ####################################################################
    #
    def stop_server(self):
        """

        """
        return

    ####################################################################
    #
    def summon_entity(self, entity, coords, data_tag):
        """
        Keyword Arguments:
        entity   --
        coords   --
        data_tag --
        """
        return

    ####################################################################
    #
    def tell(self, player, message):
        """
        Keyword Arguments:
        player  --
        message --
        """
        return

    ####################################################################
    #
    def tell_raw(self, player, raw_json_message):
        """
        Keyword Arguments:
        player           --
        raw_json_message --
        """
        return

    ####################################################################
    #
    def tp(self, player, coords):
        """
        Keyword Arguments:
        player --
        coords --
        """
        res = self.conn.send("tp %s %d %d %d" % (player, coords[0], coords[1],
                                                 coords[2]))
        return res

    ####################################################################
    #
    def get_block(self, coords):
        """
        Get the block at the given coordinates

        Keyword Arguments:
        coords     --
        """
        coords = int_floor(coords)
        res = self.conn.send("testforblock %d %d %d %s" %
                             (coords[0], coords[1], coords[2],
                              block.AIR.command_output))

        if res == "Cannot test for block outside of the world":
            raise OutsideLoadedWorld("(%d,%d,%d)" % coords)

        # If the block we tested for actually was there, then job done
        #
        if res[0:32] == "Successfully found the block at ":
            return block.AIR

        # otherwise we need to tease out what block it was, and send
        # another query to determine what data that block has.
        #
        m = Minecraft.FOUND_BLOCK.search(res)
        if m is None:
            raise UnhandledResponse("'%s' when expecting 'The block at "
                                    "%d,%d,%d is <something> (expected: "
                                    "tile.air.name).'" % coords)
        found_name = m.groups()[0]
        try:
            b = block.Block.lookup_by_name(found_name)
        except KeyError:
            raise UnknownBlock('by name "%s"' % found_name)

        # We have found which block it is. Now we need to test what its data
        # value is..
        #
        res = self.conn.send("testforblock %d %d %d %s" %
                             (coords[0], coords[1], coords[2],
                              b.command_output))

        # We either get back "Successfully found the block at " or
        # "The block at <x>,<y>,<z> had the data value of <d> (expected: 0)."
        #
        if res[0:32] == "Successfully found the block at ":
            return b

        m = Minecraft.TESTED_DATA.search(res)
        if m is None:
            raise UnhandledResponse("'%s' when expecting 'The block at "
                                    "%d,%d,%d had the data value of <d> "
                                    "(expected: 0).'" % coords)
        return block.Block.lookup_or_create(b.id, found_name,
                                            int(m.groups()[0]))

    ####################################################################
    #
    def get_blocks(self, coords0, coords1):
        """
        Queries the world for the blocks in the cuboid defined by coords0,
        coords1. Returns a SparseVolume with the results of what
        wasfound.

        Keyword Arguments:
        coords0 --
        coords1 --
        """
        x0, y0, z0 = coords0
        x1, y1, z1 = coords1
        width = int(abs(x0-x1)) + 1
        height = int(abs(y0-y1)) + 1
        depth = int(abs(z0-z1)) + 1

        sv = SparseVolume(width, height, depth)

        for y in c_range(y0, y1):
            for z in c_range(z0, z1):
                for x in c_range(x0, x1):
                    sx, sy, sz = (abs(x0 - x), abs(y0 - y), abs(z0 - z))
                    b = self.get_block((x, y, z))
                    sv.set((sx, sy, sz), b)
        return sv

    ####################################################################
    #
    def set_time(self, time):
        """
        Keyword Arguments:
        time --
        """
        return

    ####################################################################
    #
    def incr_time(self, amount):
        """
        Keyword Arguments:
        amount --
        """
        return

    ####################################################################
    #
    def get_whitelist(self):
        """

        """
        return

    ####################################################################
    #
    def enable_whitelist(self, enable=True):
        """
        Keyword Arguments:
        enable -- (default True)
        """
        return

    ####################################################################
    #
    def add_to_whitelist(self, player):
        """
        Keyword Arguments:
        player --
        """
        return

    ####################################################################
    #
    def remove_from_whitelist(self, player):
        """
        Keyword Arguments:
        player --
        """
        return

    ####################################################################
    #
    def reload_whitelist(self):
        """

        """
        return

    ####################################################################
    #
    def give_player_xp(self, player, amount):
        """
        Keyword Arguments:
        player --
        amount --
        """
        return
