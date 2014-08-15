#!/usr/bin/env python
#
# File: $Id$
#
"""
simple repl console loop
"""

# system imports
#
import getpass
import readline
import os.path
# Our imports
#
from mcrcon import mcrcon

print 'Ctrl-C to exit'
# host = raw_input('Host: ')
# port = raw_input('Port (25575): ')
# if port == '':
#     port = 25575
# else:
#     port = int(port)
# pwd = getpass.getpass('Password: ')

print "Connecting..."
r = mcrcon.MCRcon("soujya.apricot.com", 25575, "foobybooby")
print "Logged in successfully"

# Read our history file for readline, if it exists.
#
histfile = os.path.join(os.environ["HOME"], ".mcrepl")
try:
    readline.read_history_file(histfile)
except IOError:
    pass

try:
    while True:
        line = raw_input('Rcon: ')
        print r.send(line)
except KeyboardInterrupt, e:
    readline.write_history_file(histfile)
    r.close()
