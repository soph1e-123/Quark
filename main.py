import pygame
from levels import *

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

def switch_panels(current_panel, level, setups, level_index):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RETURN]:
        door_state = level.getDoor()
        new = level.get_copy()
        if new is not None:
            level = new
        level.setDoor(door_state)
        level.make_copy()
        current_panel = 0
    
    elif pressed[pygame.K_TAB]:
        level.split()
    
    elif pressed[pygame.K_r]:
        level = setups[level_index](screen_size, panel_size, BACKGROUND)
        level.make_copy()
        current_panel = 0

    if pressed[pygame.K_UP]:
        current_panel = 0

    elif pressed[pygame.K_DOWN] and level.getPanel(1) is not None:
        current_panel = 1
    
    
    return current_panel, level


def display_level_num(window, level_index):
    text = FONT.render(str(level_index+1), False, (255,181,201))
    window.blit(text, (20,20))

def next_level_text(window, screen_size):
    text = FONT.render("LEVEL COMPLETED!", False, (255,181,201))
    text_rect = text.get_rect(center=(screen_size[0]/2, screen_size[1]/2))
    window.blit(text, text_rect)


def start_screen(window, screen_size):
    running = True
    home_screen = pygame.image.load("assets/start_screen.png")
    home_screen = pygame.transform.scale(home_screen, screen_size)
    while running:
        window.blit(home_screen, (0,0))
        pygame.display.flip()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RETURN]:
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    return running


def tutorial(window, screen_size):
    running = True
    tutorial_index = 0
    #home_screen = pygame.image.load("assets/start.png")
    #home_screen = pygame.transform.scale(home_screen, screen_size[0], screen_size[1]))
    while running:
        window.blit(tutorial_screens[tutorial_index], (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tutorial_index -= 1
                    if tutorial_index < 0:
                        tutorial_index = 0
                elif event.key == pygame.K_RIGHT:
                    tutorial_index += 1
                    if tutorial_index >= len(tutorial_screens):
                        return True
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    return running

#main program

#initialise for the entire game



pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
running = True

info = pygame.display.Info()

width = info.current_h*1.6
screen_size = (width, width*0.5)

panel_size = (screen_size[0], screen_size[1]/2)
window = pygame.display.set_mode(screen_size, pygame.NOFRAME)


BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, panel_size)

end_screen = pygame.image.load("assets/end.png")
end_screen = pygame.transform.scale(end_screen, screen_size)

FONT = pygame.font.SysFont("verdana", int(screen_size[0]/20), bold=True)

current_panel = 0

tutorial_screens = []

for i in range(0,6):
    screen = pygame.image.load("assets/tutorial" + str(i)+ ".png")
    screen = pygame.transform.scale(screen, screen_size)
    tutorial_screens.append(screen)

    #--------------

    #run this for each new level

    #level_panels = [[panel1, copy(levels[0])], [panel2, copy(levels[0])]]
def main():
    
    setups = [setup_level1, setup_level2, setup_level3, setup_level4, setup_level5, setup_level6, setup_level7, setup_level8, setup_level9, setup_level10, setup_level11, setup_level12, setup_level13, setup_level15, setup_level14]
            
    current_panel = 0
    level = setups[0](screen_size, panel_size, BACKGROUND)
    level.make_copy()
    level_index = 0

    win_frame = 0

    running = start_screen(window, screen_size)

    if running:
        running = tutorial(window, screen_size)

    won = False

    finished_game = False

    while running and not finished_game:
        clock.tick(50)
        if not won:
            current_panel, level = switch_panels(current_panel, level, setups, level_index)
        player = level.getPlayer(current_panel)
        player.animate()

        if not won:
            move_player(player)
            level.checkCollisions(current_panel)

            if level.allPressed():
                level.getDoor().open()

            if player.getReset():
                level = setups[level_index](screen_size, panel_size, BACKGROUND)
                level.make_copy()
                current_panel = 0
            
            level.display(window, screen_size)
            display_level_num(window, level_index)

        if player.getWon():
            won = True
            player.animate()
            win_frame += 1
            next_level_text(window, screen_size)
        
        if win_frame > 100:
            win_frame = 0
            won = False
            level.merge()
            level_index += 1
            current_panel = 0
            if level_index < len(setups):
                level = setups[level_index](screen_size, panel_size, BACKGROUND)
                level.make_copy()
            else:
                finished_game = True

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False


    while running and finished_game:
        clock.tick(50)
        window.blit(end_screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

if __name__ == '__main__':
    main()
