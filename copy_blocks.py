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
    x, y, z = (-6, 81, -198)
    x1, y1, z1 = (2, 86, -180)
    sv = mc.get_blocks((x, y, z), (x1, y1, z1))
    mc.set_blocks_from_sparsevolume((x + 20, y, z), sv)
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
