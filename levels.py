from player import Player
from box import Box, Platform, Door
from button import Button, Bounce
from obstacle import Spike
from portal import Portal
from copy import copy
from level_class import Level
from pygame import Surface

def setup_level1(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]/2, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    box1 = Box(tile_size*5, panel_size[1], panel_size)

    button1 = Button(tile_size, panel_size[1], panel_size)
    button2 = Button(tile_size*3, panel_size[1], panel_size)
    button3 = Button(tile_size*17, panel_size[1], panel_size)
    button4 = Button(tile_size*19, panel_size[1], panel_size)

    current_objects = []

    door = Door(tile_size*14, panel_size[1], panel_size)
    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3, button4], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level2(screen_size, panel_size, BACKGROUND):
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.02, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    platform1 = Platform(tile_size*2, panel_size[1], panel_size, 3)
    platform2 = Platform(tile_size*5, panel_size[1]-tile_size, panel_size, 3)
    platform3 = Platform(tile_size*8, panel_size[1]-tile_size*2, panel_size, 3)
    platform4 = Platform(tile_size*11, panel_size[1]-tile_size*3, panel_size, 3)

    button1 = Button(tile_size*12, panel_size[1]-tile_size*4, panel_size)
    button2 = Button(tile_size*12, panel_size[1], panel_size)

    current_objects = [platform1, platform2, platform3, platform4]

    door = Door(tile_size*6, panel_size[1], panel_size)

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level3(screen_size, panel_size, BACKGROUND):
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    bounce1 = Bounce(tile_size*1.5, panel_size[1], panel_size)
    portal1 = Portal(tile_size*1.5, panel_size[1]-tile_size*1.5, panel_size)
    portal2 = Portal(tile_size*10, panel_size[1], panel_size)
    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())

    platform1 = Platform(tile_size*11, panel_size[1]-tile_size*1.5, panel_size, 3)
    platform2 = Platform(tile_size*7, panel_size[1]-tile_size*2, panel_size, 3)
    platform3 = Platform(tile_size*15, panel_size[1]-tile_size*1, panel_size, 3)

    button1 = Button(0, panel_size[1], panel_size)
    button2 = Button(tile_size*14, panel_size[1], panel_size)

    spike1 = Spike(tile_size*15.3, panel_size[1], panel_size)
    spike2 = Spike(tile_size*12.7, panel_size[1], panel_size)
    spike3 = Spike(tile_size*7.5, panel_size[1], panel_size)
    spike4 = Spike(tile_size*4.5, panel_size[1], panel_size)


    current_objects = [bounce1, spike1, spike2, spike3, spike4, portal1, portal2, platform1, platform2, platform3]

    door = Door(tile_size*6, panel_size[1], panel_size)

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level


def test_level(screen_size, panel_size, BACKGROUND):
    #set up player objects
    player1 = Player(200, screen_size[1], panel_size)
    player2 = Player(200, screen_size[1], panel_size)

    #set up objects in first panel

    box = Box(400, panel_size[1], panel_size)

    #portal2 = Portal(600, panel_size[1], panel_size)
    #portal3 = Portal(200, panel_size[1], panel_size)

    #portal2.connect(portal3.getPosition())
    #portal3.connect(portal2.getPosition())

    button = Button(500, panel_size[1], panel_size)
    platform = Platform(400, panel_size[1]-100, panel_size, 3)
    spike = Spike(800, panel_size[1], panel_size)
    door = Door(100, panel_size[1], panel_size)
    current_objects = [platform, spike, door]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button], [box], door, BACKGROUND)
    #return all objects that are part of a level
    return level