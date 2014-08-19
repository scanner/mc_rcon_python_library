#!/usr/bin/env python
#
# --------------------------------------
# This based on the script, but heavily modified by Scanner
#
#
#     Minecraft Python API
#        Castle Builder
#
#
# This script creates a castle complete
# with moat and perimeter walls.
#
# Author : Matt Hawkins
# Date   : 07/06/2014
#
# http://www.raspberrypi-spy.co.uk/
#
# --------------------------------------

# Import Minecraft libraries
from mcrcon.minecraft import Minecraft
from mcrcon import block

# --------------------------------------
# Define Functions
# --------------------------------------


########################################################################
########################################################################
#
class CastleBuilder(object):
    """
    Builds a castle at the given coordinates
    """

    ####################################################################
    #
    def __init__(self, mc, coords, num_floors):
        """
        Coordinates are the ground floor, center of the finished castle
        """
        self.center_coords = coords
        (self.x, self.y, self.z) = coords
        # We were given the coordinates of where the player was
        # standing and the ground floor for our building is the one
        # beneath their feet.
        #
        self.y -= 1
        self.floor_height = 4
        self.num_floors = num_floors
        self.keep_height = (self.floor_height * (self.num_floors+2)) + 3
        self.mc = mc

    ####################################################################
    #
    def build(self):
        print "Keep will be %d units tall" % self.keep_height
        print "Clearing space"
        # self.ClearSpace(33)
        print "Creating landscape"
        # self.CreateLandscape(33, 21)
        print "Create outer walls"
        # self.CreateWalls(19, 4, block.COBBLESTONE, block.COBBLESTONE_WALL,
        #                  True, True, True)
        print "Create Keep with 5 levels"
        self.CreateKeep(9, 5)
        return

    ####################################################################
    #
    def CreateWalls(self, size, height, material,
                    battlements=None,
                    walkway=True, torches=True, door=False):
        # Create 4 walls with a specified width, height and material.
        # Battlements and walkways can also be added to the top edges.
        x0 = round(self.x - (size/2))
        z0 = round(self.z - (size/2))
        x1 = round(self.x + (size/2))
        z1 = round(self.z + (size/2))

        y0 = self.y + 1
        y1 = self.y + height

        self.mc.set_blocks((x0, y0, z0),
                           (x0, y1, z1), material)
        self.mc.set_blocks((x0, y0, z1),
                           (x1, y1, z1), material)
        self.mc.set_blocks((x1, y0, z0),
                           (x1, y1, z1), material)
        self.mc.set_blocks((x0, y0, z0),
                           (x1, y1, z0), material)
        # Add battlements to top edge
        #
        if battlements is not None:
            self.mc.set_blocks((x0, y1+1, z0), (x0, y1+1, z1), battlements)
            self.mc.set_blocks((x0, y1+1, z0), (x1, y1+1, z0), battlements)
            self.mc.set_blocks((x1, y1+1, z1), (x0, y1+1, z1), battlements)
            self.mc.set_blocks((x1, y1+1, z1), (x1, y1+1, z0), battlements)
            for i in range(0, size, 4):
                self.mc.set_block((x0, y1+2, z0+i), block.TORCH)
                self.mc.set_block((x0+i, y1+2, z1), block.TORCH)
                self.mc.set_block((x1, y1+2, z0+i), block.TORCH)
                self.mc.set_block((x0+i, y1+2, z0), block.TORCH)

        # Add wooden walkways
        #
        if walkway is True:
            self.mc.set_blocks((x0+1, y1, z0+1), (x0+1, y1, z1-1),
                               block.PLANKS)
            self.mc.set_blocks((x0+1, y1, z1-1), (x1-1, y1, z1-1),
                               block.PLANKS)
            self.mc.set_blocks((x1-1, y1, z0+1), (x1-1, y1, z1-1),
                               block.PLANKS)
            self.mc.set_blocks((x0+1, y1, z0+1), (x1-1, y1, z0+1),
                               block.PLANKS)
            if torches:
                for i in range(2, size-2, 4):
                    # Inside along the wooden walkway
                    #
                    self.mc.set_block((x0+2, y1, z0+i), block.TORCH)
                    self.mc.set_block((x0+i, y1, z1-2), block.TORCH)
                    self.mc.set_block((x1-2, y1, z0+i), block.TORCH)
                    self.mc.set_block((x0+i, y1, z0+2), block.TORCH)

                for i in range(0, size, 4):
                    # on the outside wall
                    #
                    self.mc.set_block((x0-1, y1-1, z0+i), block.TORCH)
                    self.mc.set_block((x0+i, y1-1, z1+1), block.TORCH)
                    self.mc.set_block((x1+1, y1-1, z0+i), block.TORCH)
                    self.mc.set_block((x0+i, y1-1, z0-1), block.TORCH)

        # door..
        #
        if door is True:
            self.mc.set_block((x0, self.y+1, self.z),
                              block.WOODEN_DOOR.withData(0))
            self.mc.set_block((x0, self.y+2, self.z),
                              block.WOODEN_DOOR.withData(8))
            self.mc.set_block((x0-1, self.y+3, self.z), block.TORCH)
            self.mc.set_block((x0+1, self.y+3, self.z), block.TORCH)
            self.mc.set_block((x0-1, self.y, self.z), block.STONE)

    ####################################################################
    #
    def ClearSpace(self, size=36):
        """
        Clear space from the top all the way down to y+1

        Keyword Arguments:
        size -- (default 36)
        """
        # x, z coordinates for our outer border. This is the extent of
        # what will be cleared.
        #
        xb0 = round(self.x - (size/2))
        zb0 = round(self.z - (size/2))
        xb1 = round(self.x + (size/2))
        zb1 = round(self.z + (size/2))

        print "Clearing space"
        self.mc.set_blocks((xb0, self.y+self.keep_height, zb0),
                           (xb1, self.y+1, zb1), block.AIR)
        return

    ####################################################################
    #
    def CreateLandscape(self, outer_border=36, islandwidth=21):

        # x, z coordinates for the fence - it is 3 spaces in from the border.
        #
        #
        x0 = round(self.x - ((outer_border/2)-3))
        z0 = round(self.z - ((outer_border/2)-3))
        x1 = round(self.x + ((outer_border/2)-3))
        z1 = round(self.z + ((outer_border/2)-3))

        # # Where the 'island' is. This is the grassy court.
        # #
        # xi0 = round(self.x - (islandwidth/2))
        # zi0 = round(self.z - (islandwidth/2))
        # xi1 = round(self.x + (islandwidth/2))
        # zi1 = round(self.z + (islandwidth/2))

        # Set 2 layers beneath our base to grass, and then dirt.
        #
        print "Creating grass and dirt base centered at: (%d, %d, %d)" % \
            (self.x, self.y, self.z)
        print "         Outer x/z: (%d, %d) to (%d, %d)" % (x0, z0, z1, z1)
        self.mc.set_blocks((x0, self.y-1, z0), (x1, self.y-2, z1),
                           block.DIRT)
        self.mc.set_blocks((x0, self.y, z0), (x1, self.y-1, z1),
                           block.GRASS)

        # Create border around moat
        #
        self.mc.set_blocks((x0, self.y+1, z0),
                           (x0, self.y+1, z1),
                           block.COBBLESTONE_WALL)
        self.mc.set_blocks((x0, self.y+1, z1),
                           (x1, self.y+1, z1),
                           block.COBBLESTONE_WALL)
        self.mc.set_blocks((x1, self.y+1, z0),
                           (x1, self.y+1, z1),
                           block.COBBLESTONE_WALL)
        self.mc.set_blocks((x0, self.y+1, z0),
                           (x1, self.y+1, z0),
                           block.COBBLESTONE_WALL)

        # Torches on the cobblestone wall
        #
        for i in range(0, outer_border+2, 4):
            self.mc.set_block((x0, self.y+2, z0+i), block.TORCH)
            self.mc.set_block((x0+i, self.y+2, z1), block.TORCH)
            self.mc.set_block((x1, self.y+2, z0+i), block.TORCH)
            self.mc.set_block((x0+i, self.y+2, z0), block.TORCH)

        self.mc.set_block((x0, self.y+1, self.z),
                          block.FENCE_GATE.withData(1))
        self.mc.set_block((x0-1, self.y, self.z),
                          block.STONE)
        # Create water moat
        #
        # self.mc.set_blocks((x0+1, self.y-1, z0+1),
        #                    (x0+2, self.y-1, z0+1), block.WATER)
        # self.mc.set_blocks((x0+1, self.y-1, z0+1),
        #                    (x0+1, self.y-1, z0+1), block.WATER)
        # self.mc.set_blocks((x0+1, self.y-1, z0+1),
        #                    (x0+2, self.y-1, z0+1), block.WATER)
        # self.mc.set_blocks((x0+1, self.y-1, z0+1),
        #                    (x0+2, self.y-1, z0+1), block.WATER)

        # Create island inside moat .. do not need this since we
        # already set it up above.
        #
        # self.mc.set_blocks((xi0, self.y, zi0), (xi1, self.y, zi1),
        #                    block.GRASS)

    ####################################################################
    #
    def CreateKeep(self, size, levels):
        # Create a keep with a specified number
        # of floors levels and a roof
        height = (levels * self.floor_height) + 4
        top_floor_y = levels * self.floor_height

        self.CreateWalls(size, height, block.BRICK_BLOCK, block.FENCE,
                         True, True)

        x0 = round(self.x - (size/2))
        z0 = round(self.z - (size/2))
        x1 = round(self.x + (size/2))
        z1 = round(self.z + (size/2))

        # Floors
        #
        for level in range(0, levels + 1):
            self.mc.set_blocks((x0 + 1, (level * self.floor_height) + self.y,
                                z0 + 1),
                               (x1 - 1, (level * self.floor_height) + self.y,
                                z1 - 1),
                               block.PLANKS)
            self.CreateWindows((self.x, (level * self.floor_height) + self.y,
                                self.z), size)

        for level in range(0, levels):
            self.CreateTorches((self.x, (level * self.floor_height) + self.y,
                                self.z), size)

        # Create ladder...
        self.mc.set_blocks((x0+1, self.y+1, z0+1),
                           (x0+1, ((levels+1) * self.floor_height)+self.y,
                            z0+1),
                           block.AIR)
        self.mc.set_blocks((x0+1, self.y+1, z0+1),
                           (x0+1, ((levels+1) * self.floor_height)+self.y,
                            z0+1),
                           block.LADDER.withData(3))

        # Bed
        #
        bedroom = levels - 1
        bed_x = x0+1
        bed_y = bedroom * self.floor_height + self.y + 1
        bed_z = z1 - 1  # self.z
        self.mc.set_block((bed_x, bed_y, bed_z), block.BED.withData(1+8))
        self.mc.set_block((bed_x+1, bed_y, bed_z), block.BED.withData(1))
        print "Setting bed at (%d, %d, %d)-(%d, %d, %d)" % (bed_x, bed_y,
                                                            bed_z, bed_x+1,
                                                            bed_y, bed_z)

        # crafting block
        #
        self.mc.set_block((x1-1, bed_y, z1-1),
                          block.CRAFTING_TABLE.withData(1))

        # Furnace
        #
        self.mc.set_block((x1-1, bed_y, z1-2), block.FURNACE.withData(1))

        # Chest
        #
        self.mc.set_blocks((x1-1, bed_y, z1-3),
                           (x1-1, bed_y, z1-4),
                           block.CHEST.withData(1))

        # Doors
        #
        self.mc.set_blocks((x0, self.y+1, z1-1),
                           (x0, self.y+2, z1-1), block.AIR)
        self.mc.set_block((x0, self.y+1, z1-1), block.WOODEN_DOOR.withData(0))
        self.mc.set_block((x0, self.y+2, z1-1), block.WOODEN_DOOR.withData(8))

        # # Door
        # self.mc.set_blocks((0, baseheight + 1, size),
        #                    (0, baseheight + 2, size), block.AIR)

    ####################################################################
    #
    def CreateWindows(self, coords, size):
        hsize = size/2
        qsize = size/4
        x = coords[0]
        z = coords[2]
        x0 = round(coords[0] - hsize)
        z0 = round(coords[2] - hsize)
        x1 = round(coords[0] + hsize)
        z1 = round(coords[2] + hsize)
        y = coords[1] + 1

        # one large window per side
        #
        self.mc.set_blocks((x0, y, z+qsize), (x0, y+1, z-qsize), block.GLASS)
        self.mc.set_blocks((x1, y, z+qsize), (x1, y+1, z-qsize), block.GLASS)
        self.mc.set_blocks((x+qsize, y, z0), (x-qsize, y+1, z0), block.GLASS)
        self.mc.set_blocks((x-qsize, y, z1), (x+qsize, y+1, z1), block.GLASS)

    ####################################################################
    #
    def CreateTorches(self, coords, size):
        """
        Keyword Arguments:
        coords --
        size   --
        """
        hsize = size/2
        qsize = size/4
        (x, y, z) = coords
        y += (self.floor_height - 1)  # move the torches off of the ground
        x = coords[0]
        z = coords[2]
        x0 = round(x - hsize) + 1
        z0 = round(z - hsize) + 1
        x1 = round(x + hsize) - 1
        z1 = round(z + hsize) - 1

        self.mc.set_block((x0, y, z+qsize), block.TORCH)
        self.mc.set_block((x0, y, z-qsize), block.TORCH)

        self.mc.set_block((x1, y, z+qsize), block.TORCH)
        self.mc.set_block((x1, y, z-qsize), block.TORCH)

        self.mc.set_block((x+qsize, y, z0), block.TORCH)
        self.mc.set_block((x-qsize, y, z0), block.TORCH)

        self.mc.set_block((x+qsize, y, z1), block.TORCH)
        self.mc.set_block((x-qsize, y, z1), block.TORCH)
        return

# --------------------------------------
#
# Main Script
#
# --------------------------------------


#############################################################################
#
def main():
    # coords = (-31, 70, -203)
    # coords = (-2, 85, -191)
    # coords = (-189, 89, -120)
    # coords = (-439, 86, -47)
    # coords = (-101, 64, -380)
    # coords = (-499, 73, -655)
    # coords = (560, 64, -281)
    # coords = (966, 137, -434)
    # coords = (1264, 74, -255)
    # coords = (1249, 20, -290)
    # coords = (1298, 3, -290)
    # coords = (1501, 75, -317)
    # coords = (1864, 80, -295)
    # coords = (2115, 20, -257)
    # coords = (2284, 73, -128)
    # coords = (2682, 66, -27)
    # coords = (3328, 63, -69)
    # coords = (3677, 63, -119)
    # coords = (4339, 94, 6)
    # coords = (5022, 63, 1.4)
    # coords = (5108, 63, 236)
    # coords = (5212, 63, 216)
    # coords = (5211, 63, 281)
    # coords = (5257, 64, -47)
    # coords = (5603+(33/2), 63, 76)
    # coords = (5603+(33/2), 63, 76)
    coords = (5657, 40, 76)

    mc = Minecraft.create('foobybooby', 'soujya.apricot.com', 25575)

    mc.say("Let's build a castle!")

    cb = CastleBuilder(mc, coords, 4)
    cb.build()

    print "Position player on Keep's walkway"
    # mc.player.setPos(0, 30, 4)
    return

############################################################################
############################################################################
#
# Here is where it all starts
#
if __name__ == '__main__':
    main()
#
############################################################################
############################################################################
