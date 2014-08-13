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
    res = mc.set_block((-5, 73, -193), block.AIR)
    res = mc.set_block((-5, 73, -194), block.AIR)
    print "Result: %s" % res

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
