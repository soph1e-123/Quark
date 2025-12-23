import pygame
from player import Player
from box import Box, Platform, Door
from button import Button, Bounce
from obstacle import Spike
from portal import Portal
from copy import copy
from level_class import Level

def move_player(player):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]:
        direction = -1
    elif pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
        direction = 1
    else:
        direction = 0

    if pressed[pygame.K_SPACE] and not player.isJumping():
        player.jump(height=5)

    player.move(direction) 

def switch_panels(current_panel, level):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RETURN]:
        door_state = level.getDoor()
        new = level.get_copy()
        if new is not None:
            level = new
        level.setDoor(door_state)
        level.make_copy()
        current_panel = 0
    
    elif pressed[pygame.K_BACKSPACE]:
        level.split()
        current_panel = 1
    
    elif pressed[pygame.K_r]:
        level = setups[level_index](window)
        level.make_copy()
        current_panel = 0

    if pressed[pygame.K_1]:
        current_panel = 0

    elif pressed[pygame.K_2] and level.getPanel(1) is not None:
        current_panel = 1
    
    
    return current_panel, level


def setup_level1(window):
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

def setup_level2(window):
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

def setup_level3(window):
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


def test_level(window):
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

#main program

#initialise for the entire game


pygame.init()
clock = pygame.time.Clock()
running = True

info = pygame.display.Info()


screen_size = (info.current_h*1.6, info.current_h*0.8)

panel_size = (screen_size[0], screen_size[1]/2)
window = pygame.display.set_mode(screen_size, pygame.NOFRAME)

panel1 = pygame.Surface(panel_size)
panel1.fill((20, 20, 50))
panel2 = pygame.Surface(panel_size)
panel2.fill((50, 20, 50))

BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, panel_size)

current_panel = 0

#--------------

#run this for each new level

#level_panels = [[panel1, copy(levels[0])], [panel2, copy(levels[0])]]

setups = [setup_level1, setup_level1]

current_panel = 0
level = setups[0](window)
level.make_copy()
level_index = 0

while running:
    clock.tick(60)
    current_panel, level = switch_panels(current_panel, level)
    player = level.getPlayer(current_panel)
    player.animate()
    move_player(player)
    level.checkCollisions(current_panel)

    if level.allPressed():
        level.getDoor().open()

    if player.getWon():
        #TODO: winning animation
        level.merge()
        level_index += 1
        current_panel = 0
        if level_index < len(setups):
            level = setups[level_index](window)
            level.make_copy()
        else:
            running = False
            #TODO: won whole game
            print("you win")

    level.display(window, screen_size)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False


#TODO: quack
#TODO: merge time, split time, pause time etc
#TODO: sort out imports
#TODO: sort out global variables and parameters
#TODO: all buttons pressed -> door opens -> merge and enter door to move to next level
#TODO: keep a copy to merge back to before - mainly done, just show ghostly image
#TODO: boxes on platforms????