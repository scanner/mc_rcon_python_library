#!/usr/bin/env python
#
# File: $Id$
#
"""
Test making blocks using our API
"""

# system imports
#
import getpass

# Our imports
#
from mcrcon.minecraft import Minecraft
from mcrcon import block


#############################################################################
#
def main():
    """
    make some blocks..
    """
    # host = raw_input('Host: ')
    # port = raw_input('Port (25575): ')
    # if port == '':
    #     port = 25575
    # else:
    #     port = int(port)
    # pwd = getpass.getpass('Password: ')

    print "Connecting..."
    mc = Minecraft.create('foobybooby', 'soujya.apricot.com', 25575)
    # res = mc.set_block((-5, 73, -193), block.AIR)
    # res = mc.set_block((-5, 73, -194), block.AIR)
    # mc.set_blocks((-2, 87, -191), (-10, 87, -191), block.STONE, "replace")
    x, y, z = (-2, 87, -191)
    x1, y1, z1 = (-5, 80, -192)
    res = mc.get_block((x, y, z))
    print "Block at (%d, %d, %d) is %s" % (x, y, z, res)

    res = mc.get_blocks((x, y, z), (x1, y1, z1))
    print "Blocks in (%d, %d, %d)-(%d, %d, %d): %s" % (x, y, z, x1, y1, z1,
                                                       res)

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
