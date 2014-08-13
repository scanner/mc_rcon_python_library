#!/usr/bin/env python
#
# File: $Id$
#
"""

"""

# system imports
#


class Block:
    """Minecraft PI block description. Can be sent to Minecraft.setBlock/s"""

    ####################################################################
    #
    def __init__(self, text_id, name, data=0, data_tag=None):
        self.id = text_id
        self.name = name
        self.data = data
        self.data_tag = data_tag

    ####################################################################
    #
    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    ####################################################################
    #
    def __hash__(self):
        return self.id + str(self.data)

    ####################################################################
    #
    def withData(self, data):
        """
        XXX We need to deal with 'name' - what we will probably do is
        establish a dict by id of all the blocks with a list of the
        defined data and the associated names under each id and if
        this 'data' is in that list, we will copy that name otherwise
        the name will be set to something else..
        """
        return Block(self.id, data)

    ####################################################################
    #
    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data, self.data_tag))

    ####################################################################
    #
    def __repr__(self):
        return "Block(%s, %d)" % (self.id, self.data)

    ####################################################################
    #
    def __str__(self):
        if self.data == 0:
            return "%s" % self.id
        else:
            return "%s %d" % (self.id, self.data)

AIR = Block('minecraft:air', 'Air')
STONE = Block('minecraft:stone', 'Stone')
GRANITE = Block('minecraft:stone', 'Granite', data=1)
POLISHED_GRANITE = Block('minecraft:stone', 'Polished Granite', data=2)
DIORITE = Block('minecraft:stone', 'Diorite', data=3)
POLISHED_DIORITE = Block('minecraft:stone', 'Polished Diorite', data=4)
ANDESITE = Block('minecraft:stone', 'Andesite', data=5)
POLISHED_ANDESITE = Block('minecraft:stone', 'Polished Andesite', data=6)
GRASS = Block('minecraft:grass', 'Grass')
DIRT = Block('minecraft:dirt', 'Dirt')
COARSE_DIRT = Block('minecraft:dirt', 'Coarse Dirt', data=1)
PODZOL = Block('minecraft:dirt', 'Podzol', data=2)
COBBLESTONE = Block('minecraft:cobblestone', 'Cobblestone')
PLANKS = Block('minecraft:planks', 'Oak Wood Plank')
SPRUCE_WOOD_PLANK = Block('minecraft:planks', 'Spruce Wood Plank', data=1)
BIRCH_WOOD_PLANK = Block('minecraft:planks', 'Birch Wood Plank', data=2)
JUNGLE_WOOD_PLANK = Block('minecraft:planks', 'Jungle Wood Plank', data=3)
ACACIA_WOOD_PLANK = Block('minecraft:planks', 'Acacia Wood Plank', data=4)
DARK_OAK_WOOD_PLANK = Block('minecraft:planks', 'Dark Oak Wood Plank', data=5)
SAPLING = Block('minecraft:sapling', 'Oak Sapling')
SPRUCE_SAPLING = Block('minecraft:sapling', 'Spruce Sapling', data=1)
BIRCH_SAPLING = Block('minecraft:sapling', 'Birch Sapling', data=2)
JUNGLE_SAPLING = Block('minecraft:sapling', 'Jungle Sapling', data=3)
ACACIA_SAPLING = Block('minecraft:sapling', 'Acacia Sapling', data=4)
DARK_OAK_SAPLING = Block('minecraft:sapling', 'Dark Oak Sapling', data=5)
BEDROCK = Block('minecraft:bedrock', 'Bedrock')
FLOWING_WATER = Block('minecraft:flowing_water', 'Flowing Water')
WATER = Block('minecraft:water', 'Still Water')
FLOWING_LAVA = Block('minecraft:flowing_lava', 'Flowing Lava')
LAVA = Block('minecraft:lava', 'Still Lava')
SAND = Block('minecraft:sand', 'Sand')
RED_SAND = Block('minecraft:sand', 'Red Sand', data=1)
GRAVEL = Block('minecraft:gravel', 'Gravel')
GOLD_ORE = Block('minecraft:gold_ore', 'Gold Ore')
IRON_ORE = Block('minecraft:iron_ore', 'Iron Ore')
COAL_ORE = Block('minecraft:coal_ore', 'Coal Ore')
LOG = Block('minecraft:log', 'Oak Wood')
SPRUCE_WOOD = Block('minecraft:log', 'Spruce Wood', data=1)
BIRCH_WOOD = Block('minecraft:log', 'Birch Wood', data=2)
JUNGLE_WOOD = Block('minecraft:log', 'Jungle Wood', data=3)
LEAVES = Block('minecraft:leaves', 'Oak Leaves')
SPRUCE_LEAVES = Block('minecraft:leaves', 'Spruce Leaves', data=1)
BIRCH_LEAVES = Block('minecraft:leaves', 'Birch Leaves', data=2)
JUNGLE_LEAVES = Block('minecraft:leaves', 'Jungle Leaves', data=3)
SPONGE = Block('minecraft:sponge', 'Sponge')
WET_SPONGE = Block('minecraft:sponge', 'Wet Sponge', data=1)
GLASS = Block('minecraft:glass', 'Glass')
LAPIS_ORE = Block('minecraft:lapis_ore', 'Lapis Lazuli Ore')
LAPIS_BLOCK = Block('minecraft:lapis_block', 'Lapis Lazuli Block')
DISPENSER = Block('minecraft:dispenser', 'Dispenser')
SANDSTONE = Block('minecraft:sandstone', 'Sandstone')
CHISELED_SANDSTONE = Block('minecraft:sandstone', 'Chiseled Sandstone', data=1)
SMOOTH_SANDSTONE = Block('minecraft:sandstone', 'Smooth Sandstone', data=2)
NOTEBLOCK = Block('minecraft:noteblock', 'Note Block')
BED = Block('minecraft:bed', 'Bed')
GOLDEN_RAIL = Block('minecraft:golden_rail', 'Powered Rail')
DETECTOR_RAIL = Block('minecraft:detector_rail', 'Detector Rail')
STICKY_PISTON = Block('minecraft:sticky_piston', 'Sticky Piston')
WEB = Block('minecraft:web', 'Cobweb')
TALLGRASS = Block('minecraft:tallgrass', 'Dead Shrub')
TALLGRASS = Block('minecraft:tallgrass', 'Grass', data=1)
FERN = Block('minecraft:tallgrass', 'Fern', data=2)
DEADBUSH = Block('minecraft:deadbush', 'Dead Shrub')
PISTON = Block('minecraft:piston', 'Piston')
PISTON_HEAD = Block('minecraft:piston_head', 'Piston Head')
WOOL = Block('minecraft:wool', 'White Wool')
ORANGE_WOOL = Block('minecraft:wool', 'Orange Wool', data=1)
MAGENTA_WOOL = Block('minecraft:wool', 'Magenta Wool', data=2)
LIGHT_BLUE_WOOL = Block('minecraft:wool', 'Light Blue Wool', data=3)
YELLOW_WOOL = Block('minecraft:wool', 'Yellow Wool', data=4)
LIME_WOOL = Block('minecraft:wool', 'Lime Wool', data=5)
PINK_WOOL = Block('minecraft:wool', 'Pink Wool', data=6)
GRAY_WOOL = Block('minecraft:wool', 'Gray Wool', data=7)
LIGHT_GRAY_WOOL = Block('minecraft:wool', 'Light Gray Wool', data=8)
CYAN_WOOL = Block('minecraft:wool', 'Cyan Wool', data=9)
PURPLE_WOOL = Block('minecraft:wool', 'Purple Wool', data=10)
BLUE_WOOL = Block('minecraft:wool', 'Blue Wool', data=11)
BROWN_WOOL = Block('minecraft:wool', 'Brown Wool', data=12)
GREEN_WOOL = Block('minecraft:wool', 'Green Wool', data=13)
RED_WOOL = Block('minecraft:wool', 'Red Wool', data=14)
BLACK_WOOL = Block('minecraft:wool', 'Black Wool', data=15)
YELLOW_FLOWER = Block('minecraft:yellow_flower', 'Dandelion')
RED_FLOWER = Block('minecraft:red_flower', 'Poppy')
BLUE_ORCHID = Block('minecraft:red_flower', 'Blue Orchid', data=1)
ALLIUM = Block('minecraft:red_flower', 'Allium', data=2)
AZURE_BLUET = Block('minecraft:red_flower', 'Azure Bluet', data=3)
RED_TULIP = Block('minecraft:red_flower', 'Red Tulip', data=4)
ORANGE_TULIP = Block('minecraft:red_flower', 'Orange Tulip', data=5)
WHITE_TULIP = Block('minecraft:red_flower', 'White Tulip', data=6)
PINK_TULIP = Block('minecraft:red_flower', 'Pink Tulip', data=7)
OXEYE_DAISY = Block('minecraft:red_flower', 'Oxeye Daisy', data=8)
BROWN_MUSHROOM = Block('minecraft:brown_mushroom', 'Brown Mushroom')
RED_MUSHROOM = Block('minecraft:red_mushroom', 'Red Mushroom')
GOLD_BLOCK = Block('minecraft:gold_block', 'Gold Block')
IRON_BLOCK = Block('minecraft:iron_block', 'Iron Block')
DOUBLE_STONE_SLAB = Block('minecraft:double_stone_slab', 'Double Stone Slab')
DOUBLE_SANDSTONE_SLAB = Block('minecraft:double_stone_slab',
                              'Double Sandstone Slab', data=1)
DOUBLE_WOODEN_SLAB = Block('minecraft:double_stone_slab', 'Double Wooden Slab',
                           data=2)
DOUBLE_COBBLESTONE_SLAB = Block('minecraft:double_stone_slab',
                                'Double Cobblestone Slab', data=3)
DOUBLE_BRICK_SLAB = Block('minecraft:double_stone_slab', 'Double Brick Slab',
                          data=4)
DOUBLE_STONE_BRICK_SLAB = Block('minecraft:double_stone_slab',
                                'Double Stone Brick Slab', data=5)
DOUBLE_NETHER_BRICK_SLAB = Block('minecraft:double_stone_slab',
                                 'Double Nether Brick Slab', data=6)
DOUBLE_QUARTZ_SLAB = Block('minecraft:double_stone_slab', 'Double Quartz Slab',
                           data=7)
STONE_SLAB = Block('minecraft:stone_slab', 'Stone Slab')
SANDSTONE_SLAB = Block('minecraft:stone_slab', 'Sandstone Slab', data=1)
WOODEN_SLAB = Block('minecraft:stone_slab', 'Wooden Slab', data=2)
COBBLESTONE_SLAB = Block('minecraft:stone_slab', 'Cobblestone Slab', data=3)
BRICK_SLAB = Block('minecraft:stone_slab', 'Brick Slab', data=4)
STONE_BRICK_SLAB = Block('minecraft:stone_slab', 'Stone Brick Slab', data=5)
NETHER_BRICK_SLAB = Block('minecraft:stone_slab', 'Nether Brick Slab', data=6)
QUARTZ_SLAB = Block('minecraft:stone_slab', 'Quartz Slab', data=7)
BRICK_BLOCK = Block('minecraft:brick_block', 'Bricks')
TNT = Block('minecraft:tnt', 'TNT')
BOOKSHELF = Block('minecraft:bookshelf', 'Bookshelf')
MOSSY_COBBLESTONE = Block('minecraft:mossy_cobblestone', 'Moss Stone')
OBSIDIAN = Block('minecraft:obsidian', 'Obsidian')
TORCH = Block('minecraft:torch', 'Torch')
FIRE = Block('minecraft:fire', 'Fire')
MOB_SPAWNER = Block('minecraft:mob_spawner', 'Monster Spawner')
OAK_STAIRS = Block('minecraft:oak_stairs', 'Oak Wood Stairs')
CHEST = Block('minecraft:chest', 'Chest')
REDSTONE_WIRE = Block('minecraft:redstone_wire', 'Redstone Wire')
DIAMOND_ORE = Block('minecraft:diamond_ore', 'Diamond Ore')
DIAMOND_BLOCK = Block('minecraft:diamond_block', 'Diamond Block')
CRAFTING_TABLE = Block('minecraft:crafting_table', 'Crafting Table')
WHEAT = Block('minecraft:wheat', 'Wheat Crops')
FARMLAND = Block('minecraft:farmland', 'Farmland')
FURNACE = Block('minecraft:furnace', 'Furnace')
LIT_FURNACE = Block('minecraft:lit_furnace', 'Burning Furnace')
STANDING_SIGN = Block('minecraft:standing_sign', 'Standing Sign Block')
WOODEN_DOOR = Block('minecraft:wooden_door', 'Wooden Door Block')
LADDER = Block('minecraft:ladder', 'Ladder')
RAIL = Block('minecraft:rail', 'Rail')
STONE_STAIRS = Block('minecraft:stone_stairs', 'Cobblestone Stairs')
WALL_SIGN = Block('minecraft:wall_sign', 'Wall-mounted Sign Block')
LEVER = Block('minecraft:lever', 'Lever')
STONE_PRESSURE_PLATE = Block('minecraft:stone_pressure_plate',
                             'Stone Pressure Plate')
IRON_DOOR = Block('minecraft:iron_door', 'Iron Door Block')
WOODEN_PRESSURE_PLATE = Block('minecraft:wooden_pressure_plate',
                              'Wooden Pressure Plate')
REDSTONE_ORE = Block('minecraft:redstone_ore', 'Redstone Ore')
LIT_REDSTONE_ORE = Block('minecraft:lit_redstone_ore', 'Glowing Redstone Ore')
UNLIT_REDSTONE_TORCH = Block('minecraft:unlit_redstone_torch',
                             'Redstone Torch (off)')
REDSTONE_TORCH = Block('minecraft:redstone_torch', 'Redstone Torch (on)')
STONE_BUTTON = Block('minecraft:stone_button', 'Stone Button')
SNOW_LAYER = Block('minecraft:snow_layer', 'Snow')
ICE = Block('minecraft:ice', 'Ice')
SNOW = Block('minecraft:snow', 'Snow Block')
CACTUS = Block('minecraft:cactus', 'Cactus')
CLAY = Block('minecraft:clay', 'Clay')
REEDS = Block('minecraft:reeds', 'Sugar Canes')
JUKEBOX = Block('minecraft:jukebox', 'Jukebox')
FENCE = Block('minecraft:fence', 'Oak Fence')
PUMPKIN = Block('minecraft:pumpkin', 'Pumpkin')
NETHERRACK = Block('minecraft:netherrack', 'Netherrack')
SOUL_SAND = Block('minecraft:soul_sand', 'Soul Sand')
GLOWSTONE = Block('minecraft:glowstone', 'Glowstone')
PORTAL = Block('minecraft:portal', 'Nether Portal')
LIT_PUMPKIN = Block('minecraft:lit_pumpkin', "Jack o'Lantern")
CAKE = Block('minecraft:cake', 'Cake Block')
UNPOWERED_REPEATER = Block('minecraft:unpowered_repeater',
                           'Redstone Repeater Block (off)')
POWERED_REPEATER = Block('minecraft:powered_repeater',
                         'Redstone Repeater Block (on)')
STAINED_GLASS = Block('minecraft:stained_glass', 'White Stained Glass')
ORANGE_STAINED_GLASS = Block('minecraft:stained_glass',
                             'Orange Stained Glass', data=1)
MAGENTA_STAINED_GLASS = Block('minecraft:stained_glass',
                              'Magenta Stained Glass', data=2)
LIGHT_BLUE_STAINED_GLASS = Block('minecraft:stained_glass',
                                 'Light Blue Stained Glass', data=3)
YELLOW_STAINED_GLASS = Block('minecraft:stained_glass',
                             'Yellow Stained Glass', data=4)
LIME_STAINED_GLASS = Block('minecraft:stained_glass', 'Lime Stained Glass',
                           data=5)
PINK_STAINED_GLASS = Block('minecraft:stained_glass', 'Pink Stained Glass',
                           data=6)
GRAY_STAINED_GLASS = Block('minecraft:stained_glass', 'Gray Stained Glass',
                           data=7)
LIGHT_GRAY_STAINED_GLASS = Block('minecraft:stained_glass',
                                 'Light Gray Stained Glass', data=8)
CYAN_STAINED_GLASS = Block('minecraft:stained_glass', 'Cyan Stained Glass',
                           data=9)
PURPLE_STAINED_GLASS = Block('minecraft:stained_glass', 'Purple Stained Glass',
                             data=10)
BLUE_STAINED_GLASS = Block('minecraft:stained_glass', 'Blue Stained Glass',
                           data=11)
BROWN_STAINED_GLASS = Block('minecraft:stained_glass', 'Brown Stained Glass',
                            data=12)
GREEN_STAINED_GLASS = Block('minecraft:stained_glass', 'Green Stained Glass',
                            data=13)
RED_STAINED_GLASS = Block('minecraft:stained_glass', 'Red Stained Glass',
                          data=14)
BLACK_STAINED_GLASS = Block('minecraft:stained_glass', 'Black Stained Glass',
                            data=15)
TRAPDOOR = Block('minecraft:trapdoor', 'Wooden Trapdoor')
MONSTER_EGG = Block('minecraft:monster_egg', 'Stone Monster Egg')
COBBLESTONE_MONSTER_EGG = Block('minecraft:monster_egg',
                                'Cobblestone Monster Egg', data=1)
STONE_BRICK_MONSTER_EGG = Block('minecraft:monster_egg',
                                'Stone Brick Monster Egg', data=2)
MOSSY_STONE_BRICK_MONSTER_EGG = Block('minecraft:monster_egg',
                                      'Mossy Stone Brick Monster Egg', data=3)
CRACKED_STONE_BRICK_MONSTER_EGG = Block('minecraft:monster_egg',
                                        'Cracked Stone Brick Monster Egg',
                                        data=4)
CHISELED_STONE_BRICK_MONSTER_EGG = Block('minecraft:monster_egg',
                                         'Chiseled Stone Brick Monster Egg',
                                         data=5)
STONEBRICK = Block('minecraft:stonebrick', 'Stone Bricks')
MOSSY_STONE_BRICKS = Block('minecraft:stonebrick', 'Mossy Stone Bricks',
                           data=1)
CRACKED_STONE_BRICKS = Block('minecraft:stonebrick', 'Cracked Stone Bricks',
                             data=2)
CHISELED_STONE_BRICKS = Block('minecraft:stonebrick', 'Chiseled Stone Bricks',
                              data=3)
STONEBRICK = Block('minecraft:stonebrick', 'Red Mushroom Cap')
STONEBRICK = Block('minecraft:stonebrick', 'Brown Mushroom Cap')
IRON_BARS = Block('minecraft:iron_bars', 'Iron Bars')
GLASS_PANE = Block('minecraft:glass_pane', 'Glass Pane')
MELON_BLOCK = Block('minecraft:melon_block', 'Melon Block')
PUMPKIN_STEM = Block('minecraft:pumpkin_stem', 'Pumpkin Stem')
MELON_STEM = Block('minecraft:melon_stem', 'Melon Stem')
VINE = Block('minecraft:vine', 'Vines')
FENCE_GATE = Block('minecraft:fence_gate', 'Oak Fence Gate')
BRICK_STAIRS = Block('minecraft:brick_stairs', 'Brick Stairs')
STONE_BRICK_STAIRS = Block('minecraft:stone_brick_stairs',
                           'Stone Brick Stairs')
MYCELIUM = Block('minecraft:mycelium', 'Mycelium')
WATERLILY = Block('minecraft:waterlily', 'Lily Pad')
NETHER_BRICK = Block('minecraft:nether_brick', 'Nether Brick')
NETHER_BRICK_FENCE = Block('minecraft:nether_brick_fence',
                           'Nether Brick Fence')
NETHER_BRICK_STAIRS = Block('minecraft:nether_brick_stairs',
                            'Nether Brick Stairs')
NETHER_WART = Block('minecraft:nether_wart', 'Nether Wart')
ENCHANTING_TABLE = Block('minecraft:enchanting_table', 'Enchantment Table')
BREWING_STAND = Block('minecraft:brewing_stand', 'Brewing Stand')
CAULDRON = Block('minecraft:cauldron', 'Cauldron')
END_PORTAL = Block('minecraft:end_portal', 'End Portal')
END_PORTAL_FRAME = Block('minecraft:end_portal_frame', 'End Portal Frame')
END_STONE = Block('minecraft:end_stone', 'End Stone')
DRAGON_EGG = Block('minecraft:dragon_egg', 'Dragon Egg')
REDSTONE_LAMP = Block('minecraft:redstone_lamp', 'Redstone Lamp (inactive)')
LIT_REDSTONE_LAMP = Block('minecraft:lit_redstone_lamp',
                          'Redstone Lamp (active)')
DOUBLE_WOODEN_SLAB = Block('minecraft:double_wooden_slab',
                           'Double Oak Wood Slab')
DOUBLE_SPRUCE_WOOD_SLAB = Block('minecraft:double_wooden_slab',
                                'Double Spruce Wood Slab', data=1)
DOUBLE_BIRCH_WOOD_SLAB = Block('minecraft:double_wooden_slab',
                               'Double Birch Wood Slab', data=2)
DOUBLE_JUNGLE_WOOD_SLAB = Block('minecraft:double_wooden_slab',
                                'Double Jungle Wood Slab', data=3)
DOUBLE_ACACIA_WOOD_SLAB = Block('minecraft:double_wooden_slab',
                                'Double Acacia Wood Slab', data=4)
DOUBLE_DARK_OAK_WOOD_SLAB = Block('minecraft:double_wooden_slab',
                                  'Double Dark Oak Wood Slab', data=5)
WOODEN_SLAB = Block('minecraft:wooden_slab', 'Oak Wood Slab')
SPRUCE_WOOD_SLAB = Block('minecraft:wooden_slab', 'Spruce Wood Slab', data=1)
BIRCH_WOOD_SLAB = Block('minecraft:wooden_slab', 'Birch Wood Slab', data=2)
JUNGLE_WOOD_SLAB = Block('minecraft:wooden_slab', 'Jungle Wood Slab', data=3)
ACACIA_WOOD_SLAB = Block('minecraft:wooden_slab', 'Acacia Wood Slab', data=4)
DARK_OAK_WOOD_SLAB = Block('minecraft:wooden_slab', 'Dark Oak Wood Slab',
                           data=5)
COCOA = Block('minecraft:cocoa', 'Cocoa')
SANDSTONE_STAIRS = Block('minecraft:sandstone_stairs', 'Sandstone Stairs')
EMERALD_ORE = Block('minecraft:emerald_ore', 'Emerald Ore')
ENDER_CHEST = Block('minecraft:ender_chest', 'Ender Chest')
TRIPWIRE_HOOK = Block('minecraft:tripwire_hook', 'Tripwire Hook')
TRIPWIRE_HOOK = Block('minecraft:tripwire_hook', 'Tripwire')
EMERALD_BLOCK = Block('minecraft:emerald_block', 'Emerald Block')
SPRUCE_STAIRS = Block('minecraft:spruce_stairs', 'Spruce Wood Stairs')
BIRCH_STAIRS = Block('minecraft:birch_stairs', 'Birch Wood Stairs')
JUNGLE_STAIRS = Block('minecraft:jungle_stairs', 'Jungle Wood Stairs')
COMMAND_BLOCK = Block('minecraft:command_block', 'Command Block')
BEACON = Block('minecraft:beacon', 'Beacon')
COBBLESTONE_WALL = Block('minecraft:cobblestone_wall', 'Cobblestone Wall')
MOSSY_COBBLESTONE_WALL = Block('minecraft:cobblestone_wall',
                               'Mossy Cobblestone Wall', data=1)
FLOWER_POT = Block('minecraft:flower_pot', 'Flower Pot')
CARROTS = Block('minecraft:carrots', 'Carrots')
POTATOES = Block('minecraft:potatoes', 'Potatoes')
WOODEN_BUTTON = Block('minecraft:wooden_button', 'Wooden Button')
SKULL = Block('minecraft:skull', 'Mob Head')
ANVIL = Block('minecraft:anvil', 'Anvil')
TRAPPED_CHEST = Block('minecraft:trapped_chest', 'Trapped Chest')
LIGHT_WEIGHTED_PRESSURE_PLATE = Block(
    'minecraft:light_weighted_pressure_plate',
    'Weighted Pressure Plate (light)')
HEAVY_WEIGHTED_PRESSURE_PLATE = Block(
    'minecraft:heavy_weighted_pressure_plate',
    'Weighted Pressure Plate (heavy)')
UNPOWERED_COMPARATOR = Block('minecraft:unpowered_comparator',
                             'Redstone Comparator (inactive)')
POWERED_COMPARATOR = Block('minecraft:powered_comparator',
                           'Redstone Comparator (active)')
DAYLIGHT_DETECTOR = Block('minecraft:daylight_detector', 'Daylight Sensor')
REDSTONE_BLOCK = Block('minecraft:redstone_block', 'Redstone Block')
QUARTZ_ORE = Block('minecraft:quartz_ore', 'Nether Quartz Ore')
HOPPER = Block('minecraft:hopper', 'Hopper')
QUARTZ_BLOCK = Block('minecraft:quartz_block', 'Quartz Block')
CHISELED_QUARTZ_BLOCK = Block('minecraft:quartz_block',
                              'Chiseled Quartz Block', data=1)
PILLAR_QUARTZ_BLOCK = Block('minecraft:quartz_block',
                            'Pillar Quartz Block', data=2)
QUARTZ_STAIRS = Block('minecraft:quartz_stairs', 'Quartz Stairs')
ACTIVATOR_RAIL = Block('minecraft:activator_rail', 'Activator Rail')
DROPPER = Block('minecraft:dropper', 'Dropper')
STAINED_HARDENED_CLAY = Block('minecraft:stained_hardened_clay',
                              'White Stained Clay')
ORANGE_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                            'Orange Stained Clay', data=1)
MAGENTA_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                             'Magenta Stained Clay', data=2)
LIGHT_BLUE_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                                'Light Blue Stained Clay', data=3)
YELLOW_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                            'Yellow Stained Clay', data=4)
LIME_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                          'Lime Stained Clay', data=5)
PINK_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                          'Pink Stained Clay', data=6)
GRAY_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                          'Gray Stained Clay', data=7)
LIGHT_GRAY_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                                'Light Gray Stained Clay', data=8)
CYAN_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                          'Cyan Stained Clay', data=9)
PURPLE_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                            'Purple Stained Clay', data=10)
BLUE_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                          'Blue Stained Clay', data=11)
BROWN_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                           'Brown Stained Clay', data=12)
GREEN_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                           'Green Stained Clay', data=13)
RED_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                         'Red Stained Clay', data=14)
BLACK_STAINED_CLAY = Block('minecraft:stained_hardened_clay',
                           'Black Stained Clay', data=15)
STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                           'White Stained Glass Pane')
ORANGE_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                  'Orange Stained Glass Pane', data=1)
MAGENTA_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                   'Magenta Stained Glass Pane', data=2)
LIGHT_BLUE_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                      'Light Blue Stained Glass Pane', data=3)
YELLOW_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                  'Yellow Stained Glass Pane', data=4)
LIME_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                'Lime Stained Glass Pane', data=5)
PINK_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                'Pink Stained Glass Pane', data=6)
GRAY_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                'Gray Stained Glass Pane', data=7)
LIGHT_GRAY_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                      'Light Gray Stained Glass Pane', data=8)
CYAN_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                'Cyan Stained Glass Pane', data=9)
PURPLE_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                  'Purple Stained Glass Pane', data=10)
BLUE_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                'Blue Stained Glass Pane', data=11)
BROWN_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                 'Brown Stained Glass Pane', data=12)
GREEN_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                 'Green Stained Glass Pane', data=13)
RED_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                               'Red Stained Glass Pane', data=14)
BLACK_STAINED_GLASS_PANE = Block('minecraft:stained_glass_pane',
                                 'Black Stained Glass Pane', data=15)
LEAVES2 = Block('minecraft:leaves2', 'Acacia Leaves')
DARK_OAK_LEAVES = Block('minecraft:leaves2', 'Dark Oak Leaves', data=1)
LOGS2 = Block('minecraft:logs2', 'Acacia Wood')
DARK_OAK_WOOD = Block('minecraft:logs2', 'Dark Oak Wood', data=1)
ACACIA_STAIRS = Block('minecraft:acacia_stairs', 'Acacia Wood Stairs')
DARK_OAK_STAIRS = Block('minecraft:dark_oak_stairs', 'Dark Oak Wood Stairs')
SLIME = Block('minecraft:slime', 'Slime Block')
BARRIER = Block('minecraft:barrier', 'Barrier')
IRON_TRAPDOOR = Block('minecraft:iron_trapdoor', 'Iron Trapdoor')
PRISMARINE = Block('minecraft:prismarine', 'Prismarine')
PRISMARINE_BRICKS = Block('minecraft:prismarine', 'Prismarine Bricks', data=1)
DARK_PRISMARINE = Block('minecraft:prismarine', 'Dark Prismarine', data=2)
SEA_LANTERN = Block('minecraft:sea_lantern', 'Sea Lantern')
HAY_BLOCK = Block('minecraft:hay_block', 'Hay Bale')
CARPET = Block('minecraft:carpet', 'White Carpet')
ORANGE_CARPET = Block('minecraft:carpet', 'Orange Carpet', data=1)
MAGENTA_CARPET = Block('minecraft:carpet', 'Magenta Carpet', data=2)
LIGHT_BLUE_CARPET = Block('minecraft:carpet', 'Light Blue Carpet', data=3)
YELLOW_CARPET = Block('minecraft:carpet', 'Yellow Carpet', data=4)
LIME_CARPET = Block('minecraft:carpet', 'Lime Carpet', data=5)
PINK_CARPET = Block('minecraft:carpet', 'Pink Carpet', data=6)
GRAY_CARPET = Block('minecraft:carpet', 'Gray Carpet', data=7)
LIGHT_GRAY_CARPET = Block('minecraft:carpet', 'Light Gray Carpet', data=8)
CYAN_CARPET = Block('minecraft:carpet', 'Cyan Carpet', data=9)
PURPLE_CARPET = Block('minecraft:carpet', 'Purple Carpet', data=10)
BLUE_CARPET = Block('minecraft:carpet', 'Blue Carpet', data=11)
BROWN_CARPET = Block('minecraft:carpet', 'Brown Carpet', data=12)
GREEN_CARPET = Block('minecraft:carpet', 'Green Carpet', data=13)
RED_CARPET = Block('minecraft:carpet', 'Red Carpet', data=14)
BLACK_CARPET = Block('minecraft:carpet', 'Black Carpet', data=15)
HARDENED_CLAY = Block('minecraft:hardened_clay', 'Hardened Clay')
COAL_BLOCK = Block('minecraft:coal_block', 'Block of Coal')
PACKED_ICE = Block('minecraft:packed_ice', 'Packed Ice')
DOUBLE_PLANT = Block('minecraft:double_plant', 'Sunflower')
LILAC = Block('minecraft:double_plant', 'Lilac', data=1)
DOUBLE_TALLGRASS = Block('minecraft:double_plant', 'Double Tallgrass', data=2)
LARGE_FERN = Block('minecraft:double_plant', 'Large Fern', data=3)
ROSE_BUSH = Block('minecraft:double_plant', 'Rose Bush', data=4)
PEONY = Block('minecraft:double_plant', 'Peony', data=5)
STANDING_BANNER = Block('minecraft:standing_banner', 'Free-standing Banner')
WALL_BANNER = Block('minecraft:wall_banner', 'Wall-mounted Banner')
DAYLIGHT_DETECTOR_INVERTED = Block('minecraft:daylight_detector_inverted',
                                   'Inverted Daylight Sensor')
RED_SANDSTONE = Block('minecraft:red_sandstone', 'Red Sandstone')
SMOOTH_RED_SANDSTONE = Block('minecraft:red_sandstone', 'Smooth Red Sandstone',
                             data=1)
CHISELED_RED_SANDSTONE = Block('minecraft:red_sandstone',
                               'Chiseled Red Sandstone', data=2)
RED_SANDSTONE_STAIRS = Block('minecraft:red_sandstone_stairs',
                             'Red Sandstone Stairs')
STONE_SLAB2 = Block('minecraft:stone_slab2', 'Double Red Sandstone Slab')
DOUBLE_STONE_SLAB2 = Block('minecraft:double_stone_slab2',
                           'Red Sandstone Slab')
SPRUCE_FENCE_GATE = Block('minecraft:spruce_fence_gate', 'Spruce Fence Gate')
BIRCH_FENCE_GATE = Block('minecraft:birch_fence_gate', 'Birch Fence Gate')
JUNGLE_FENCE_GATE = Block('minecraft:jungle_fence_gate', 'Jungle Fence Gate')
DARK_OAK_FENCE_GATE = Block('minecraft:dark_oak_fence_gate',
                            'Dark Oak Fence Gate')
ACACIA_FENCE_GATE = Block('minecraft:acacia_fence_gate', 'Acacia Fence Gate')
SPRUCE_FENCE = Block('minecraft:spruce_fence', 'Spruce Fence')
BIRCH_FENCE = Block('minecraft:birch_fence', 'Birch Fence')
JUNGLE_FENCE = Block('minecraft:jungle_fence', 'Jungle Fence')
DARK_OAK_FENCE = Block('minecraft:dark_oak_fence', 'Dark Oak Fence')
ACACIA_FENCE = Block('minecraft:acacia_fence', 'Acacia Fence')
SPRUCE_DOOR = Block('minecraft:spruce_door', 'Spure Door Block')
BIRCH_DOOR = Block('minecraft:birch_door', 'Birch Door Block')
JUNGLE_DOOR = Block('minecraft:jungle_door', 'Jungle Door Block')
ACACIA_DOOR = Block('minecraft:acacia_door', 'Acacia Door Block')
DARK_OAK_DOOR = Block('minecraft:dark_oak_door', 'Dark Oak Door Block')
IRON_SHOVEL = Block('minecraft:iron_shovel', 'Iron Shovel')
IRON_PICKAXE = Block('minecraft:iron_pickaxe', 'Iron Pickaxe')
IRON_AXE = Block('minecraft:iron_axe', 'Iron Axe')
FLINT_AND_STEEL = Block('minecraft:flint_and_steel', 'Flint and Steel')
APPLE = Block('minecraft:apple', 'Apple')
BOW = Block('minecraft:bow', 'Bow')
ARROW = Block('minecraft:arrow', 'Arrow')
COAL = Block('minecraft:coal', 'Coal')
CHARCOAL = Block('minecraft:coal', 'Charcoal', data=1)
DIAMOND = Block('minecraft:diamond', 'Diamond')
IRON_INGOT = Block('minecraft:iron_ingot', 'Iron Ingot')
GOLD_INGOT = Block('minecraft:gold_ingot', 'Gold Ingot')
IRON_SWORD = Block('minecraft:iron_sword', 'Iron Sword')
WOODEN_SWORD = Block('minecraft:wooden_sword', 'Wooden Sword')
WOODEN_SHOVEL = Block('minecraft:wooden_shovel', 'Wooden Shovel')
WOODEN_PICKAXE = Block('minecraft:wooden_pickaxe', 'Wooden Pickaxe')
WOODEN_AXE = Block('minecraft:wooden_axe', 'Wooden Axe')
STONE_SWORD = Block('minecraft:stone_sword', 'Stone Sword')
STONE_SHOVEL = Block('minecraft:stone_shovel', 'Stone Shovel')
STONE_PICKAXE = Block('minecraft:stone_pickaxe', 'Stone Pickaxe')
STONE_AXE = Block('minecraft:stone_axe', 'Stone Axe')
DIAMOND_SWORD = Block('minecraft:diamond_sword', 'Diamond Sword')
DIAMOND_SHOVEL = Block('minecraft:diamond_shovel', 'Diamond Shovel')
DIAMOND_PICKAXE = Block('minecraft:diamond_pickaxe', 'Diamond Pickaxe')
DIAMOND_AXE = Block('minecraft:diamond_axe', 'Diamond Axe')
STICK = Block('minecraft:stick', 'Stick')
BOWL = Block('minecraft:bowl', 'Bowl')
MUSHROOM_STEW = Block('minecraft:mushroom_stew', 'Mushroom Stew')
GOLDEN_SWORD = Block('minecraft:golden_sword', 'Golden Sword')
GOLDEN_SHOVEL = Block('minecraft:golden_shovel', 'Golden Shovel')
GOLDEN_PICKAXE = Block('minecraft:golden_pickaxe', 'Golden Pickaxe')
GOLDEN_AXE = Block('minecraft:golden_axe', 'Golden Axe')
STRING = Block('minecraft:string', 'String')
FEATHER = Block('minecraft:feather', 'Feather')
GUNPOWDER = Block('minecraft:gunpowder', 'Gunpowder')
WOODEN_HOE = Block('minecraft:wooden_hoe', 'Wooden Hoe')
STONE_HOE = Block('minecraft:stone_hoe', 'Stone Hoe')
IRON_HOE = Block('minecraft:iron_hoe', 'Iron Hoe')
DIAMOND_HOE = Block('minecraft:diamond_hoe', 'Diamond Hoe')
GOLDEN_HOE = Block('minecraft:golden_hoe', 'Golden Hoe')
WHEAT_SEEDS = Block('minecraft:wheat_seeds', 'Wheat Seeds')
WHEAT = Block('minecraft:wheat', 'Wheat')
BREAD = Block('minecraft:bread', 'Bread')
LEATHER_HELMET = Block('minecraft:leather_helmet', 'Leather Helmet')
LEATHER_CHESTPLATE = Block('minecraft:leather_chestplate', 'Leather Tunic')
LEATHER_LEGGINGS = Block('minecraft:leather_leggings', 'Leather Pants')
LEATHER_BOOTS = Block('minecraft:leather_boots', 'Leather Boots')
CHAINMAIL_HELMET = Block('minecraft:chainmail_helmet', 'Chainmail Helmet')
CHAINMAIL_CHESTPLATE = Block('minecraft:chainmail_chestplate',
                             'Chainmail Chestplate')
CHAINMAIL_LEGGINGS = Block('minecraft:chainmail_leggings',
                           'Chainmail Leggings')
CHAINMAIL_BOOTS = Block('minecraft:chainmail_boots', 'Chainmail Boots')
IRON_HELMET = Block('minecraft:iron_helmet', 'Iron Helmet')
IRON_CHESTPLATE = Block('minecraft:iron_chestplate', 'Iron Chestplate')
IRON_LEGGINGS = Block('minecraft:iron_leggings', 'Iron Leggings')
IRON_BOOTS = Block('minecraft:iron_boots', 'Iron Boots')
DIAMOND_HELMET = Block('minecraft:diamond_helmet', 'Diamond Helmet')
DIAMOND_CHESTPLATE = Block('minecraft:diamond_chestplate',
                           'Diamond Chestplate')
DIAMOND_LEGGINGS = Block('minecraft:diamond_leggings', 'Diamond Leggings')
DIAMOND_BOOTS = Block('minecraft:diamond_boots', 'Diamond Boots')
GOLDEN_HELMET = Block('minecraft:golden_helmet', 'Golden Helmet')
GOLDEN_CHESTPLATE = Block('minecraft:golden_chestplate', 'Golden Chestplate')
GOLDEN_LEGGINGS = Block('minecraft:golden_leggings', 'Golden Leggings')
GOLDEN_BOOTS = Block('minecraft:golden_boots', 'Golden Boots')
FLINT_AND_STEEL = Block('minecraft:flint_and_steel', 'Flint')
PORKCHOP = Block('minecraft:porkchop', 'Raw Porkchop')
COOKED_PORKCHOP = Block('minecraft:cooked_porkchop', 'Cooked Porkchop')
PAINTING = Block('minecraft:painting', 'Painting')
GOLDEN_APPLE = Block('minecraft:golden_apple', 'Golden Apple')
ENCHANTED_GOLDEN_APPLE = Block('minecraft:golden_apple',
                               'Enchanted Golden Apple', data=1)
SIGN = Block('minecraft:sign', 'Sign')
WOODEN_DOOR = Block('minecraft:wooden_door', 'Wooden Door')
BUCKET = Block('minecraft:bucket', 'Bucket')
WATER_BUCKET = Block('minecraft:water_bucket', 'Water Bucket')
LAVA_BUCKET = Block('minecraft:lava_bucket', 'Lava Bucket')
MINECART = Block('minecraft:minecart', 'Minecart')
SADDLE = Block('minecraft:saddle', 'Saddle')
IRON_DOOR = Block('minecraft:iron_door', 'Iron Door')
REDSTONE = Block('minecraft:redstone', 'Redstone')
SNOWBALL = Block('minecraft:snowball', 'Snowball')
BOAT = Block('minecraft:boat', 'Boat')
LEATHER = Block('minecraft:leather', 'Leather')
MILK_BUCKET = Block('minecraft:milk_bucket', 'Milk Bucket')
BRICK = Block('minecraft:brick', 'Brick')
CLAY_BALL = Block('minecraft:clay_ball', 'Clay')
REEDS = Block('minecraft:reeds', 'Sugar Canes')
PAPER = Block('minecraft:paper', 'Paper')
BOOK = Block('minecraft:book', 'Book')
SLIME_BALL = Block('minecraft:slime_ball', 'Slimeball')
CHEST_MINECART = Block('minecraft:chest_minecart', 'Minecart with Chest')
FURNACE_MINECART = Block('minecraft:furnace_minecart', 'Minecart with Furnace')
EGG = Block('minecraft:egg', 'Egg')
COMPASS = Block('minecraft:compass', 'Compass')
FISHING_ROD = Block('minecraft:fishing_rod', 'Fishing Rod')
CLOCK = Block('minecraft:clock', 'Clock')
GLOWSTONE_DUST = Block('minecraft:glowstone_dust', 'Glowstone Dust')
FISH = Block('minecraft:fish', 'Raw Fish')
RAW_SALMON = Block('minecraft:fish', 'Raw Salmon', data=1)
CLOWNFISH = Block('minecraft:fish', 'Clownfish', data=2)
PUFFERFISH = Block('minecraft:fish', 'Pufferfish', data=3)
COOKED_FISH = Block('minecraft:cooked_fish', 'Cooked Fish')
COOKED_SALMON = Block('minecraft:cooked_fish', 'Cooked Salmon', data=1)
DYE = Block('minecraft:dye', 'Ink Sack')
ROSE_RED = Block('minecraft:dye', 'Rose Red', data=1)
CACTUS_GREEN = Block('minecraft:dye', 'Cactus Green', data=2)
COCO_BEANS = Block('minecraft:dye', 'Coco Beans', data=3)
LAPIS_LAZULI = Block('minecraft:dye', 'Lapis Lazuli', data=4)
PURPLE_DYE = Block('minecraft:dye', 'Purple Dye', data=5)
CYAN_DYE = Block('minecraft:dye', 'Cyan Dye', data=6)
LIGHT_GRAY_DYE = Block('minecraft:dye', 'Light Gray Dye', data=7)
GRAY_DYE = Block('minecraft:dye', 'Gray Dye', data=8)
PINK_DYE = Block('minecraft:dye', 'Pink Dye', data=9)
LIME_DYE = Block('minecraft:dye', 'Lime Dye', data=10)
DANDELION_YELLOW = Block('minecraft:dye', 'Dandelion Yellow', data=11)
LIGHT_BLUE_DYE = Block('minecraft:dye', 'Light Blue Dye', data=12)
MAGENTA_DYE = Block('minecraft:dye', 'Magenta Dye', data=13)
ORANGE_DYE = Block('minecraft:dye', 'Orange Dye', data=14)
BONE_MEAL = Block('minecraft:dye', 'Bone Meal', data=15)
BONE = Block('minecraft:bone', 'Bone')
SUGAR = Block('minecraft:sugar', 'Sugar')
CAKE = Block('minecraft:cake', 'Cake')
BED = Block('minecraft:bed', 'Bed')
REPEATER = Block('minecraft:repeater', 'Redstone Repeater')
COOKIE = Block('minecraft:cookie', 'Cookie')
FILLED_MAP = Block('minecraft:filled_map', 'Map')
SHEARS = Block('minecraft:shears', 'Shears')
MELON = Block('minecraft:melon', 'Melon')
PUMPKIN_SEEDS = Block('minecraft:pumpkin_seeds', 'Pumpkin Seeds')
MELON_SEEDS = Block('minecraft:melon_seeds', 'Melon Seeds')
BEEF = Block('minecraft:beef', 'Raw Beef')
COOKED_BEEF = Block('minecraft:cooked_beef', 'Steak')
CHICKEN = Block('minecraft:chicken', 'Raw Chicken')
COOKED_CHICKEN = Block('minecraft:cooked_chicken', 'Cooked Chicken')
ROTTEN_FLESH = Block('minecraft:rotten_flesh', 'Rotten Flesh')
ENDER_PEARL = Block('minecraft:ender_pearl', 'Ender Pearl')
BLAZE_ROD = Block('minecraft:blaze_rod', 'Blaze Rod')
GHAST_TEAR = Block('minecraft:ghast_tear', 'Ghast Tear')
GOLD_NUGGET = Block('minecraft:gold_nugget', 'Gold Nugget')
NETHER_WART = Block('minecraft:nether_wart', 'Nether Wart')
POTION = Block('minecraft:potion', 'Potion')
GLASS_BOTTLE = Block('minecraft:glass_bottle', 'Glass Bottle')
SPIDER_EYE = Block('minecraft:spider_eye', 'Spider Eye')
FERMENTED_SPIDER_EYE = Block('minecraft:fermented_spider_eye',
                             'Fermented Spider Eye')
BLAZE_POWDER = Block('minecraft:blaze_powder', 'Blaze Powder')
MAGMA_CREAM = Block('minecraft:magma_cream', 'Magma Cream')
BREWING_STAND = Block('minecraft:brewing_stand', 'Brewing Stand')
CAULDRON = Block('minecraft:cauldron', 'Cauldron')
ENDER_EYE = Block('minecraft:ender_eye', 'Eye of Ender')
SPECKLED_MELON = Block('minecraft:speckled_melon', 'Glistering Melon')
SPAWN_CREEPER = Block('minecraft:spawn_egg', 'Spawn Creeper', data=50)
SPAWN_SKELETON = Block('minecraft:spawn_egg', 'Spawn Skeleton', data=51)
SPAWN_SPIDER = Block('minecraft:spawn_egg', 'Spawn Spider', data=52)
SPAWN_ZOMBIE = Block('minecraft:spawn_egg', 'Spawn Zombie', data=54)
SPAWN_SLIME = Block('minecraft:spawn_egg', 'Spawn Slime', data=55)
SPAWN_GHAST = Block('minecraft:spawn_egg', 'Spawn Ghast', data=56)
SPAWN_PIGMAN = Block('minecraft:spawn_egg', 'Spawn Pigman', data=57)
SPAWN_ENDERMAN = Block('minecraft:spawn_egg', 'Spawn Enderman', data=58)
SPAWN_CAVE_SPIDER = Block('minecraft:spawn_egg', 'Spawn Cave Spider', data=59)
SPAWN_SILVERFISH = Block('minecraft:spawn_egg', 'Spawn Silverfish', data=60)
SPAWN_BLAZE = Block('minecraft:spawn_egg', 'Spawn Blaze', data=61)
SPAWN_MAGMA_CUBE = Block('minecraft:spawn_egg', 'Spawn Magma Cube', data=62)
SPAWN_BAT = Block('minecraft:spawn_egg', 'Spawn Bat', data=65)
SPAWN_WITCH = Block('minecraft:spawn_egg', 'Spawn Witch', data=66)
SPAWN_ENDERMITE = Block('minecraft:spawn_egg', 'Spawn Endermite', data=67)
SPAWN_GUARDIAN = Block('minecraft:spawn_egg', 'Spawn Guardian', data=68)
SPAWN_PIG = Block('minecraft:spawn_egg', 'Spawn Pig', data=90)
SPAWN_SHEEP = Block('minecraft:spawn_egg', 'Spawn Sheep', data=91)
SPAWN_COW = Block('minecraft:spawn_egg', 'Spawn Cow', data=92)
SPAWN_CHICKEN = Block('minecraft:spawn_egg', 'Spawn Chicken', data=93)
SPAWN_SQUID = Block('minecraft:spawn_egg', 'Spawn Squid', data=94)
SPAWN_WOLF = Block('minecraft:spawn_egg', 'Spawn Wolf', data=95)
SPAWN_MOOSHROOM = Block('minecraft:spawn_egg', 'Spawn Mooshroom', data=96)
SPAWN_OCELOT = Block('minecraft:spawn_egg', 'Spawn Ocelot', data=98)
SPAWN_HORSE = Block('minecraft:spawn_egg', 'Spawn Horse', data=100)
SPAWN_RABBIT = Block('minecraft:spawn_egg', 'Spawn Rabbit', data=101)
SPAWN_VILLAGER = Block('minecraft:spawn_egg', 'Spawn Villager', data=120)
EXPERIENCE_BOTTLE = Block('minecraft:experience_bottle',
                          "Bottle o' Enchanting")
FIRE_CHARGE = Block('minecraft:fire_charge', 'Fire Charge')
WRITABLE_BOOK = Block('minecraft:writable_book', 'Book and Quill')
WRITTEN_BOOK = Block('minecraft:written_book', 'Written Book')
EMERALD = Block('minecraft:emerald', 'Emerald')
ITEM_FRAME = Block('minecraft:item_frame', 'Item Frame')
FLOWER_POT = Block('minecraft:flower_pot', 'Flower Pot')
CARROT = Block('minecraft:carrot', 'Carrot')
POTATO = Block('minecraft:potato', 'Potato')
BAKED_POTATO = Block('minecraft:baked_potato', 'Baked Potato')
POISONOUS_POTATO = Block('minecraft:poisonous_potato', 'Poisonous Potato')
MAP = Block('minecraft:map', 'Empty Map')
GOLDEN_CARROT = Block('minecraft:golden_carrot', 'Golden Carrot')
SKULL = Block('minecraft:skull', 'Mob Head (Skeleton)')
MOB_HEAD_WITHER_SKELETON = Block('minecraft:skull',
                                 'Mob Head (Wither Skeleton)', data=1)
MOB_HEAD_ZOMBIE = Block('minecraft:skull', 'Mob Head (Zombie)', data=2)
MOB_HEAD_HUMAN = Block('minecraft:skull', 'Mob Head (Human)', data=3)
MOB_HEAD_CREEPER = Block('minecraft:skull', 'Mob Head (Creeper)', data=4)
CARROT_ON_A_STICK = Block('minecraft:carrot_on_a_stick', 'Carrot on a Stick')
NETHER_STAR = Block('minecraft:nether_star', 'Nether Star')
PUMPKIN_PIE = Block('minecraft:pumpkin_pie', 'Pumpkin Pie')
FIREWORKS = Block('minecraft:fireworks', 'Firework Rocket')
FIREWORK_CHARGE = Block('minecraft:firework_charge', 'Firework Star')
ENCHANTED_BOOK = Block('minecraft:enchanted_book', 'Enchanted Book')
COMPARATOR = Block('minecraft:comparator', 'Redstone Comparator')
NETHERBRICK = Block('minecraft:netherbrick', 'Nether Brick')
QUARTZ = Block('minecraft:quartz', 'Nether Quartz')
TNT_MINECART = Block('minecraft:tnt_minecart', 'Minecart with TNT')
HOPPER_MINECART = Block('minecraft:hopper_minecart', 'Minecart with Hopper')
PRISMARINE_SHARD = Block('minecraft:prismarine_shard', 'Prismarine Shard')
PRISMARINE_CRYSTALS = Block('minecraft:prismarine_crystals',
                            'Prismarine Crystals')
RABBIT = Block('minecraft:rabbit', 'Raw Rabbit')
COOKED_RABBIT = Block('minecraft:cooked_rabbit', 'Cooked Rabbit')
RABBIT_STEW = Block('minecraft:rabbit_stew', 'Rabbit Stew')
RABBIT_FOOT = Block('minecraft:rabbit_foot', "Rabbit's Foot")
RABBIT_HIDE = Block('minecraft:rabbit_hide', 'Rabbit Hide')
ARMOR_STAND = Block('minecraft:armor_stand', 'Armor Stand')
IRON_HORSE_ARMOR = Block('minecraft:iron_horse_armor', 'Iron Horse Armor')
GOLDEN_HORSE_ARMOR = Block('minecraft:golden_horse_armor',
                           'Golden Horse Armor')
DIAMOND_HORSE_ARMOR = Block('minecraft:diamond_horse_armor',
                            'Diamond Horse Armor')
LEAD = Block('minecraft:lead', 'Lead')
NAME_TAG = Block('minecraft:name_tag', 'Name Tag')
COMMAND_BLOCK_MINECART = Block('minecraft:command_block_minecart',
                               'Minecart with Command Block')
MUTTON = Block('minecraft:mutton', 'Raw Mutton')
COOKED_MUTTON = Block('minecraft:cooked_mutton', 'Cooked Mutton')
BANNER = Block('minecraft:banner', 'Banner')
SPRUCE_DOOR = Block('minecraft:spruce_door', 'Spruce Door')
BIRCH_DOOR = Block('minecraft:birch_door', 'Birch Door')
JUNGLE_DOOR = Block('minecraft:jungle_door', 'Jungle Door')
ACACIA_DOOR = Block('minecraft:acacia_door', 'Acacia Door')
DARK_OAK_DOOR = Block('minecraft:dark_oak_door', 'Dark Oak Door')
RECORD_13 = Block('minecraft:record_13', '13 Disc')
RECORD_CAT = Block('minecraft:record_cat', 'Cat Disc')
RECORD_BLOCKS = Block('minecraft:record_blocks', 'Blocks Disc')
RECORD_CHIRP = Block('minecraft:record_chirp', 'Chirp Disc')
RECORD_FAR = Block('minecraft:record_far', 'Far Disc')
RECORD_MALL = Block('minecraft:record_mall', 'Mall Disc')
RECORD_MELLOHI = Block('minecraft:record_mellohi', 'Mellohi Disc')
RECORD_STAL = Block('minecraft:record_stal', 'Stal Disc')
RECORD_STRAD = Block('minecraft:record_strad', 'Strad Disc')
RECORD_WARD = Block('minecraft:record_ward', 'Ward Disc')
RECORD_11 = Block('minecraft:record_11', '11 Disc')
RECORD_WAIT = Block('minecraft:record_wait', 'Wait Disc')
