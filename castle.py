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
        self.mc = mc

    ####################################################################
    #
    def build(self):
        print "Create ground and moat"
        self.CreateLandscape(34, 36, 26)

        print "Create outer walls"
        self.CreateWalls(26, 4, block.BRICK_BLOCK, True, True)

        print "Create inner walls"
        self.CreateWalls(16, 5, block.BRICK_BLOCK, True, True)

        print "Create Keep with 4 levels"
        self.CreateKeep(8, 4)
        return

    ####################################################################
    #
    def CreateWalls(self, size, height, material, battlements,
                    walkway):
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
        if battlements is True:
            for i in range(0, size, 2):
                self.mc.set_block((x0, y1 + 1, z0 + i), material)
                self.mc.set_block((x0 + i, y1 + 1, z1), material)
                self.mc.set_block((x1, y1 + 1, z0 + i), material)
                self.mc.set_block((x0 + i, y1 + 1, z0), material)

        # Add wooden walkways
        if walkway is True:
            self.mc.set_blocks((x0+1, y1-1, z0+1),
                               (x0+1, y1-1, z1-1), block.PLANKS)
            self.mc.set_blocks((x0+1, y1-1, z1-1),
                               (x1-1, y1-1, z1-1), block.PLANKS)
            self.mc.set_blocks((x1-1, y1-1, z0+1),
                               (x1-1, y1-1, z1-1), block.PLANKS)
            self.mc.set_blocks((x0+1, y1-1, z0+1),
                               (x1-1, y1-1, z0+1), block.PLANKS)

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

        self.mc.set_blocks((x0-1, self.y, z0-1), (x1+1, self.y+30, z1+1),
                           block.AIR)

        # Set 2 layers beneath our base to grass, and then dirt.
        #
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

    def CreateKeep(self, size, levels):
        # Create a keep with a specified number
        # of floors levels and a roof
        height = (levels * 4) + 4

        self.CreateWalls(size, height, block.BRICK_BLOCK, True,
                         True)

        x0 = round(self.x - (size/2))
        z0 = round(self.z - (size/2))
        x1 = round(self.x + (size/2))
        z1 = round(self.z + (size/2))

        # Floors & Windows
        for level in range(1, levels + 1):
            self.mc.set_blocks((x0 + 1, (level * 4) + self.y, z0 + 1),
                               (x1 - 1, (level * 4) + self.y, z1 - 1),
                               block.PLANKS)

        # Windows
        for level in range(1, levels + 1):
            self.CreateWindows(0, (level * 4) + self.y + 2, size, "N")
            self.CreateWindows(0, (level * 4) + self.y + 2, -size, "S")
            self.CreateWindows(-size, (level * 4) + self.y + 2, 0, "W")
            self.CreateWindows(size, (level * 4) + self.y + 2, 0, "E")

        # # Door
        # self.mc.set_blocks((0, baseheight + 1, size),
        #                    (0, baseheight + 2, size), block.AIR)

    def CreateWindows(self, x, y, z, dir):
        if dir in ("N", "S"):
            z1 = z
            z2 = z
            x1 = x - 2
            x2 = x + 2

        if dir in ("E", "W"):
            z1 = z - 2
            z2 = z + 2
            x1 = x
            x2 = x

        self.mc.set_blocks((x1, y, z1), (x1, y + 1, z1), block.AIR)
        self.mc.set_blocks((x2, y, z2), (x2, y + 1, z2), block.AIR)

        if dir == "N":
            a = 3
        if dir == "S":
            a = 2
        if dir == "W":
            a = 0
        if dir == "E":
            a = 1

        self.mc.set_block((x1, y - 1, z1), block.WOOL)
        self.mc.set_block((x2, y - 1, z2), block.WOOL)

# --------------------------------------
#
# Main Script
#
# --------------------------------------


#############################################################################
#
def main():
    coords = (-31, 70, -203)

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
