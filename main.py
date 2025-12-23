import pygame
from levels import setup_level1, setup_level2, setup_level3, setup_level4

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
        level = setups[level_index](screen_size, panel_size, BACKGROUND)
        level.make_copy()
        current_panel = 0

    if pressed[pygame.K_1]:
        current_panel = 0

    elif pressed[pygame.K_2] and level.getPanel(1) is not None:
        current_panel = 1
    
    
    return current_panel, level


def display_level_num(window, level_index):
    text = FONT.render(str(level_index+1), False, (255,255,255))
    window.blit(text, (20,20))

#main program

#initialise for the entire game


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
running = True

info = pygame.display.Info()

screen_size = (info.current_h*1.6, info.current_h*0.8)

panel_size = (screen_size[0], screen_size[1]/2)
window = pygame.display.set_mode(screen_size, pygame.NOFRAME)


BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, panel_size)
FONT = pygame.font.SysFont("verdana", int(screen_size[0]/20), bold=True)

current_panel = 0

#--------------

#run this for each new level

#level_panels = [[panel1, copy(levels[0])], [panel2, copy(levels[0])]]

setups = [setup_level4, setup_level2, setup_level3]

current_panel = 0
level = setups[0](screen_size, panel_size, BACKGROUND)
level.make_copy()
level_index = 0

while running:
    clock.tick(50)
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
            level = setups[level_index](screen_size, panel_size, BACKGROUND)
            level.make_copy()
        else:
            running = False
            #TODO: won whole game
            print("you win")

    level.display(window, screen_size)
    display_level_num(window, level_index)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False


#TODO: quack
#TODO: merge time, split time, pause time etc
#TODO: sort out imports
#TODO: optimise in general (improve frame rate etc)
#TODO: sort out global variables and parameters
#TODO: all buttons pressed -> door opens -> merge and enter door to move to next level
#TODO: keep a copy to merge back to before - mainly done, just show ghostly image
#TODO: boxes on platforms????