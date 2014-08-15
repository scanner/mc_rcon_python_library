#!/usr/bin/python
# --------------------------------------
#
#     Minecraft Python API
#        Castle Builder
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
    def __init__(self, mc, coords):
        """
        Coordinates are the ground floor, center of the finished castle
        """
        self.center_coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.floor_height = 4
        self.num_floors = 4
        self.keep_height = (self.floor_height * (self.num_floors+1)) + 1
        self.mc = mc

    ####################################################################
    #
    def build(self):
        print "Create ground and moat"
        self.CreateLandscape(34, 36, 27)

        # print "Create outer walls"
        self.CreateWalls(27, 4, block.COBBLESTONE, block.COBBLESTONE_WALL,
                         True)

        # print "Create inner walls"
        # self.CreateWalls(16, 5, block.BRICK_BLOCK, True, True)

        print "Create Keep with 5 levels"
        self.CreateKeep(9, 5)
        return

    ####################################################################
    #
    def PlaceBed(self):
        return

    ####################################################################
    #
    def PlaceFurnace(self):
        return

    ####################################################################
    #
    def PlaceCraftingTable(self):
        return

    ####################################################################
    #
    def PlaceChest(self):
        return

    ####################################################################
    #
    def CreateWalls(self, size, height, material,
                    battlements=None,
                    walkway=True, torches=True):
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

    ####################################################################
    #
    def CreateLandscape(self, moatwidth, moatdepth, islandwidth):
        # Set everything above our base layer to air
        #
        x0 = round(self.x - (moatwidth/2))
        z0 = round(self.z - (moatdepth/2))
        x1 = round(self.x + (moatwidth/2))
        z1 = round(self.z + (moatdepth/2))

        xi0 = round(self.x - (islandwidth/2))
        zi0 = round(self.z - (islandwidth/2))
        xi1 = round(self.x + (islandwidth/2))
        zi1 = round(self.z + (islandwidth/2))
        print "Clearing space"
        self.mc.set_blocks((x0-1, self.y+self.keep_height, z0-1),
                           (x1+1, self.y, z1+1),
                           block.AIR)

        # Set 2 layers beneath our base to grass, and then dirt.
        #
        print "Creating grass and dirt base"
        self.mc.set_blocks((x0-1, self.y-2, z0-1), (x1+1, self.y-2, z1+1),
                           block.DIRT)
        self.mc.set_blocks((x0-1, self.y-1, z0-1), (x1+1, self.y-1, z1+1),
                           block.GRASS)

        # Create border around moat
        #
        self.mc.set_blocks((x0-1, self.y, z0-1),
                           (x0-1, self.y, z1+1),
                           block.GRASS)
        self.mc.set_blocks((x0-1, self.y, z1+1),
                           (x1+1, self.y, z1+1),
                           block.GRASS)
        self.mc.set_blocks((x1+1, self.y, z0-1),
                           (x1+1, self.y, z1+1),
                           block.GRASS)
        self.mc.set_blocks((x0-1, self.y, z0-1),
                           (x1+1, self.y, z0-1),
                           block.GRASS)
        # Create water moat
        #
        self.mc.set_blocks((x0, self.y, z0), (x1, self.y, z1), block.WATER)

        # Create island inside moat
        #
        self.mc.set_blocks((xi0, self.y, zi0), (xi1, self.y, zi1),
                           block.GRASS)

    ####################################################################
    #
    def CreateKeep(self, size, levels):
        # Create a keep with a specified number
        # of floors levels and a roof
        height = (levels * self.floor_height) + 4

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
                           (x0+1, (levels * self.floor_height)+self.y, z0+1),
                           block.AIR)
        self.mc.set_blocks((x0+1, self.y+1, z0+1),
                           (x0+1, (levels * self.floor_height)+self.y, z0+1),
                           block.LADDER.withData(3))

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
        x = coords[0]
        z = coords[2]
        x0 = round(coords[0] - hsize) + 1
        z0 = round(coords[2] - hsize) + 1
        x1 = round(coords[0] + hsize) - 1
        z1 = round(coords[2] + hsize) - 1
        y = coords[1] + 3

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
    # coords = (-189, 89, -120)
    # coords = (-439, 86, -47)
    coords = (-101, 64, -380)
    mc = Minecraft.create('foobybooby', 'soujya.apricot.com', 25575)

    mc.say("Let's build a castle!")

    cb = CastleBuilder(mc, coords)
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
