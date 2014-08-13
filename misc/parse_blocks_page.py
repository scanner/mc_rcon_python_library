#!/usr/bin/env python
#
# File: $Id$
#
"""
grungy little script to parse the block data out of
http://minecraft-ids.grahamedgecombe.com
"""

# system imports
#
from bs4 import BeautifulSoup


#############################################################################
#
def main():
    soup = BeautifulSoup(open("mcrcon/blocks.html"))
    for tr in soup.find_all('tr'):
        id = tr.find(
            lambda x: x.has_attr('class') and 'id' in x['class']
        ).string
        name = tr.find(
            lambda x: x.has_attr('class') and 'name' in x['class']
        ).string
        text_id = tr.find(
            lambda x: x.has_attr('class') and 'text-id' in x['class']
        ).string
        text_id = text_id[1:-1]
        block_name = text_id.split(':')[1].upper()
        data = 0

        # If this block has an id other than 0, we need to fiddle the
        # block name to be based on the name of the block instead of
        # its text id (because all blocks with the same type have the
        # same text id.. the data makes them different..)
        #
        # Furthermore if the block name after all that is 'GRASS' we
        # need to switch back to the 'text_id' because
        # minecraft:tallgrass's name is GRASS' which is already used
        # by the block named 'GRASS'
        #
        if ':' in id:
            data = int(id.split(':')[1])
            block_name = name.upper().replace(' ', '_')
            if block_name == "GRASS":
                block_name = "TALLGRASS"

        # Get rid of any parents in our block names...
        #
        block_name = block_name.replace('(', '').replace(')', '')
        if data != 0:
            print "%s = Block('%s', \"%s\", data=%d)" % (block_name, text_id,
                                                         name, data)
        else:
            print "%s = Block('%s', \"%s\")" % (block_name, text_id, name)
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
