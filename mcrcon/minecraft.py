#!/usr/bin/env python
#
# File: $Id$
#
"""
Our API for manipulating the minecraft server through rcon. We
expose the commands that minecraft supports over rcon as methods on a
class.

"""

# system imports
#
import math

# 3rd party imports
#

# our module imports
#
import mcrcon
from util import flatten
from vec3 import Vec3

SURVIVAL = 'survival'
CREATIVE = 'creative'
ADVENTURE = 'adventure'

SCOREBOARD_PLAYERS = 'players'
SCOREBOARD_OBJECTIVES = 'objectives'
SCOREBOARD_TEAMS = 'teams'

BLOCK_KEEP = "keep"
BLOCK_DESTROY = "destroy"
BLOCK_REPLACE = "replace"


####################################################################
#
def intFloor(*args):
    return [int(math.floor(x)) for x in flatten(args)]


########################################################################
########################################################################
#
class Minecraft(object):
    """
    API interface to minecraft server via rcon
    """

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
    def set_achievment(self, achievment, player):
        """
        Keyword Arguments:
        achievment --
        player     --
        """
        pass

    ####################################################################
    #
    def ban_player(self, player):
        """
        Keyword Arguments:
        player --
        """
        pass

    ####################################################################
    #
    def ban_ip(self, ip_address):
        """
        Keyword Arguments:
        ip_address --
        """
        pass

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
        Keyword Arguments:
        player --
        item   -- (default None)
        data   -- (default None)
        """
        return

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
    def give_player_item(self, player, item, amount=1, data=None,
                         data_tag=None):
        """
        Keyword Arguments:
        player   --
        item     --
        amount   -- (default 1)
        data     -- (default None)
        data_tag -- (default None)
        """
        return

    ####################################################################
    #
    def kick_player(self, playe, reason=None):
        """
        Keyword Arguments:
        playe  --
        reason -- (default None)
        """
        return

    ####################################################################
    #
    def kill(self):
        """

        """
        return

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
        return

    ####################################################################
    #
    def pardon_player(self, player):
        """
        Keyword Arguments:
        player --
        """
        return

    ####################################################################
    #
    def pardon_ip(self, ip_address):
        """
        Keyword Arguments:
        ip_address --
        """
        return

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
        return

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
        coords = intFloor(coords)
        res = self.conn.send("setblock %d %d %d %s" % (coords[0],
                                                       coords[1],
                                                       coords[2],
                                                       block))
        return res

    ####################################################################
    #
    def set_blocks(self, coords0, coords1, block,
                   old_block_handling="replace"):
        """
        Set a cuboid of blocks (x0,y0,z0),(x1,y1,z1),block

        Keyword Arguments:
        coords0             --
        coords1             --
        block               --
        old_block_handling  -- (default "replace") Specifies how to handle the
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
        # Since the cuboid is inclusive from coords0 to coords1 we need to
        # make sure the ranges we generate run the full gamut of numbers.
        #
        x0, y0, z0 = coords0
        x1, y1, z1 = coords1

        ####################################################################
        #
        def c_range(i, j):
            """
            Range the two values so we produce an inclusive range()
            """
            i = int(i)
            j = int(j)
            if i > j:
                i += 1
                for k in range(j, i):
                    yield k
            else:
                j += 1
                for k in range(i, j):
                    yield k

        for y in c_range(y0, y1):
            for z in c_range(z0, z1):
                for x in c_range(x0, x1):
                    self.set_block((x, y, z), block, old_block_handling)
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
    def test_for_player(self, player):
        """
        Keyword Arguments:
        player --
        """
        return

    ####################################################################
    #
    def get_block(self, coords):
        """
        Keyword Arguments:
        coords     --
        """
        return

    ####################################################################
    #
    def get_blocks(self, coords0, coords1):
        """
        Keyword Arguments:
        coords0 --
        coords1 --
        """
        return

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
