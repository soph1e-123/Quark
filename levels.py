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


def setup_level4(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    box1 = Box(tile_size*4, panel_size[1], panel_size)

    button1 = Button(tile_size*15, panel_size[1], panel_size)
    button2 = Button(tile_size*18.5, panel_size[1]-tile_size*1.75, panel_size)

    spike1 = Spike(tile_size*17, panel_size[1], panel_size)
    spike2 = Spike(tile_size*17, panel_size[1]-tile_size*1.75, panel_size)
    spike3 = Spike(tile_size, panel_size[1]-tile_size*1.75, panel_size)

    portal1 = Portal(tile_size*12, panel_size[1]-tile_size*3, panel_size)
    portal2 = Portal(tile_size*18.5, panel_size[1]-tile_size*4, panel_size)
    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())

    door = Door(tile_size*18.5, panel_size[1], panel_size)
    platform1 = Platform(-tile_size*0.5,panel_size[1]-tile_size*0.75, panel_size, 2.5)
    platform2 = Platform(tile_size*17, panel_size[1]-tile_size*0.75, panel_size, 3.5)

    current_objects = [spike1, spike2, spike3, portal1, portal2, platform1, platform2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level5(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    box1 = Box(tile_size*10, panel_size[1], panel_size)

    button1 = Button(tile_size*12, panel_size[1], panel_size)
    button2 = Button(tile_size*15, panel_size[1], panel_size)
    button3 = Button(tile_size*8, panel_size[1]-tile_size*3, panel_size)

    spike1 = Spike(tile_size*13.5, panel_size[1], panel_size)
    spike2 = Spike(tile_size*16.5, panel_size[1], panel_size)


    portal1 = Portal(tile_size*4, panel_size[1], panel_size)
    portal2 = Portal(tile_size*15, panel_size[1]-tile_size*4, panel_size)
    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())
    
    portal3 = Portal(tile_size*16.5, panel_size[1]-tile_size*2.2, panel_size)
    portal4 = Portal(tile_size*8, panel_size[1]-tile_size*4, panel_size)
    portal3.connect(portal4.getPosition())
    portal4.connect(portal3.getPosition())

    door = Door(tile_size*8, panel_size[1], panel_size)

    platform1 = Platform(tile_size*7.5,panel_size[1]-tile_size*2, panel_size, 2)

    current_objects = [spike1, spike2, portal1, portal2, portal3, portal4, platform1]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level6(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    button1 = Button(tile_size, panel_size[1]-tile_size*3, panel_size)
    button2 = Button(tile_size*18, panel_size[1]-tile_size*3, panel_size)

    portal1 = Portal(tile_size*3, panel_size[1]-tile_size*3, panel_size)
    portal2 = Portal(tile_size*17, panel_size[1]-tile_size*3, panel_size)
    portal3 = Portal(tile_size*4, panel_size[1], panel_size)
    portal3.connect(portal1.getPosition())
    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())

    door = Door(tile_size*2, panel_size[1], panel_size)

    platform1 = Platform(-tile_size,panel_size[1]-tile_size*2, panel_size, 22)

    current_objects = [portal1, portal2, portal3, platform1]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level7(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    box1 = Box(tile_size*2, panel_size[1], panel_size)
    bounce1 = Bounce(tile_size*4, panel_size[1], panel_size)

    platform1 = Platform(tile_size*5, panel_size[1]-tile_size*3, panel_size, 2.5)
    platform2 = Platform(tile_size*11.5, panel_size[1]-tile_size*1.5, panel_size, 2.5)
    spike1 = Spike(tile_size*7.5, panel_size[1], panel_size)
    spike2 = Spike(tile_size*10.5, panel_size[1], panel_size)

    button1 = Button(tile_size*6, panel_size[1]-tile_size*4, panel_size)
    button2 = Button(tile_size*12.5, panel_size[1]-tile_size*2.5, panel_size)
    button3 = Button(tile_size*16, panel_size[1], panel_size)

    door = Door(tile_size*9, panel_size[1], panel_size)

    current_objects = [spike1, spike2, bounce1, platform1, platform2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level8(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel
    bounce1 = Bounce(tile_size*4, panel_size[1], panel_size)
    bounce2 = Bounce(tile_size*14, panel_size[1], panel_size)

    button1 = Button(tile_size*4, panel_size[1]-tile_size*4, panel_size)
    button2 = Button(tile_size*14, panel_size[1]-tile_size*4, panel_size)

    door = Door(tile_size*9, panel_size[1]-tile_size*2, panel_size)

    box1 = Box(tile_size*7, panel_size[1], panel_size)

    current_objects = [bounce1, bounce2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level9(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    button1 = Button(tile_size, panel_size[1]-tile_size*3.5, panel_size)
    button2 = Button(tile_size*2.5, panel_size[1]-tile_size*2, panel_size)

    door = Door(tile_size*9, panel_size[1]-tile_size*2.5, panel_size)
    platform1 = Platform(tile_size*8, panel_size[1]-tile_size*1.5, panel_size, 3)
    platform2 = Platform(tile_size, panel_size[1]-tile_size*2.5, panel_size, 1)
    platform3 = Platform(tile_size*2.5, panel_size[1]-tile_size, panel_size, 1)
    spike1 = Spike(tile_size*2.5, panel_size[1], panel_size)
    spike2 = Spike(tile_size*3.5, panel_size[1], panel_size)

    box1 = Box(tile_size*15, panel_size[1], panel_size)

    current_objects = [platform1, platform2, platform3, spike1, spike2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level10(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, screen_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    button1 = Button(tile_size*1.5, panel_size[1]-tile_size*2, panel_size)
    button2 = Button(tile_size*17.5, panel_size[1]-tile_size*2, panel_size)

    door = Door(tile_size*9, panel_size[1], panel_size)
    platform1 = Platform(0, panel_size[1]-tile_size, panel_size, 4)
    platform2 = Platform(tile_size*16, panel_size[1]-tile_size, panel_size, 4)

    spike1 = Spike(tile_size*0, panel_size[1]-tile_size*2, panel_size)
    spike2 = Spike(tile_size*3, panel_size[1]-tile_size*2, panel_size)
    spike3 = Spike(tile_size*16, panel_size[1]-tile_size*2, panel_size)
    spike4 = Spike(tile_size*19, panel_size[1]-tile_size*2, panel_size)

    portal1 = Portal(tile_size*1.5, panel_size[1]-tile_size*4, panel_size)
    portal2 = Portal(tile_size*17.5, panel_size[1]-tile_size*4, panel_size)

    portal3 = Portal(tile_size*1.5, panel_size[1], panel_size)
    portal4 = Portal(tile_size*17.5, panel_size[1], panel_size)
    portal5 = Portal(tile_size*9, panel_size[1]-tile_size*1.5, panel_size)

    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())

    portal3.connect(portal1.getPosition())
    portal4.connect(portal5.getPosition())

    current_objects = [platform1, platform2, spike1, spike2, spike3, spike4, portal1, portal2, portal3, portal4, portal5]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level11(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.35, panel_size[1]*0.2, panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    button1 = Button(0, panel_size[1], panel_size)
    button2 = Button(tile_size*5, panel_size[1], panel_size)
    button3 = Button(tile_size*2, panel_size[1], panel_size)

    door = Door(tile_size*18, panel_size[1]-tile_size*3, panel_size)

    platform1 = Platform(-tile_size*0.5, panel_size[1]-tile_size*2, panel_size, 5)
    platform2 = Platform(tile_size*6, panel_size[1]-tile_size*3, panel_size, 2)
    platform3 = Platform(tile_size*18, panel_size[1]-tile_size*2, panel_size, 3)

    spike1 = Spike(tile_size*3.5, panel_size[1], panel_size)
    spike2 = Spike(tile_size*6.5, panel_size[1], panel_size)

    box1 = Box(tile_size*9, panel_size[1],panel_size)


    current_objects = [platform1, platform2, platform3, spike1, spike2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level12(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, panel_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    button1 = Button(tile_size*2, panel_size[1]-tile_size*2.5, panel_size)
    button2 = Button(tile_size*18, panel_size[1], panel_size)
    button3 = Button(tile_size*2, panel_size[1], panel_size)

    door = Door(tile_size*17, panel_size[1]-tile_size*2.5, panel_size)

    platform1 = Platform(-tile_size*0.5, panel_size[1]-tile_size*1.5, panel_size, 5)
    platform2 = Platform(tile_size*16, panel_size[1]-tile_size*1.5, panel_size, 5)

    spike1 = Spike(tile_size*15, panel_size[1], panel_size)

    box1 = Box(tile_size*3, panel_size[1],panel_size)
    portal1 = Portal(tile_size*16, panel_size[1], panel_size)
    portal2 = Portal(tile_size*19, panel_size[1]-tile_size*2.5, panel_size)

    portal1.connect(portal2.getPosition())
    portal2.connect(portal1.getPosition())

    current_objects = [platform1, platform2, spike1, portal1, portal2]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3], [box1], door, BACKGROUND)
    #return all objects that are part of a level
    return level


def setup_level13(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(0, panel_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    door = Door(tile_size*9.5, panel_size[1], panel_size)

    platform1 = Platform(tile_size, panel_size[1]-tile_size*3, panel_size, 1)
    button1 = Button(tile_size, panel_size[1]-tile_size*4, panel_size)
    button2 = Button(tile_size*18, panel_size[1]-tile_size*4, panel_size)
    platform2 = Platform(tile_size*18, panel_size[1]-tile_size*3, panel_size, 1)

    bounce1 = Bounce(tile_size*4, panel_size[1], panel_size)
    bounce2 = Bounce(tile_size*6, panel_size[1]-tile_size*2, panel_size)
    bounce3 = Bounce(tile_size*13, panel_size[1]-tile_size*2, panel_size)
    bounce4 = Bounce(tile_size*15, panel_size[1], panel_size)

    portal1 = Portal(tile_size*8, panel_size[1]-tile_size*3, panel_size)
    portal2 = Portal(tile_size*11, panel_size[1]-tile_size*3, panel_size)

    portal3 = Portal(tile_size, -tile_size*3, panel_size)
    portal4 = Portal(tile_size*18, -tile_size*3, panel_size)

    portal1.connect(portal3.getPosition())
    portal2.connect(portal4.getPosition())

    current_objects = [platform1, platform2, portal1, portal2, portal3, portal4, bounce1, bounce2, bounce3, bounce4]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level14(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, panel_size[1]*0.4, panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    door = Door(tile_size*9.5, panel_size[1]-tile_size*3, panel_size)
    platform1 = Platform(tile_size*8.5, panel_size[1]-tile_size*2,panel_size,3)

    spike1 = Spike(tile_size*8.5, panel_size[1], panel_size)
    spike2 = Spike(tile_size*9.5, panel_size[1], panel_size)
    spike3 = Spike(tile_size*10.5, panel_size[1], panel_size)
    button1 = Button(tile_size*11.5, panel_size[1], panel_size)
    box1 = Box(tile_size*13, panel_size[1], panel_size)
    button2 = Button(tile_size*14.5, panel_size[1], panel_size)
    spike4 = Spike(tile_size*15.5, panel_size[1], panel_size)

    button3 = Button(tile_size*7.5, panel_size[1], panel_size)
    box2 = Box(tile_size*6, panel_size[1], panel_size)
    button4 = Button(tile_size*4.5, panel_size[1], panel_size)
    spike5 = Spike(tile_size*3.5, panel_size[1], panel_size)

    current_objects = [spike1, spike2, spike3, spike4, spike5, platform1]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2, button3, button4], [box1, box2], door, BACKGROUND)
    #return all objects that are part of a level
    return level

def setup_level15(screen_size, panel_size, BACKGROUND):
    #set up panel
    panel1 = Surface(panel_size)
    #set up player objects
    player1 = Player(screen_size[0]*0.45, panel_size[1], panel_size)
    #20 tiles on the screen
    tile_size = player1.getSize()[0]

    #set up objects in first panel

    door = Door(tile_size*9.5, panel_size[1]-tile_size*3, panel_size)

    platform1 = Platform(-0.5*tile_size, panel_size[1]-tile_size, panel_size, 2.5)
    platform2 = Platform(tile_size*3, panel_size[1], panel_size, 2)
    platform3 = Platform(tile_size*17, panel_size[1]-tile_size, panel_size, 3.5)
    platform4 = Platform(tile_size*14, panel_size[1]-tile_size*2, panel_size, 2)
    platform5 = Platform(tile_size*18, panel_size[1]-tile_size*3, panel_size, 2.5)
    platform6 = Platform(tile_size*-0.5, panel_size[1]-tile_size*3, panel_size, 2.5)
    platform7 = Platform(tile_size*7.5, panel_size[1]-tile_size*2, panel_size, 5)
    platform8 = Platform(tile_size*3, panel_size[1]-tile_size*3, panel_size, 3.5)

    button1 = Button(tile_size, panel_size[1]-tile_size*4, panel_size)
    button2 = Button(tile_size*18, panel_size[1]-tile_size*4, panel_size)

    current_objects = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8]

    objects = [[],[]]
    for item in current_objects:
        objects[0].append(copy(item))
        objects[1].append(copy(item))

    level = Level(player1, objects[0], panel1, [button1, button2], [], door, BACKGROUND)
    #return all objects that are part of a level
    return level