import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create two "panels"
    panel1 = pygame.Surface((400, 600))
    panel1.fill((255, 0, 0))
    panel2 = pygame.Surface((400, 600))
    panel2.fill((0, 0, 255))
    panel1.blit()

    screen.blit(panel1, (0, 0))
    screen.blit(panel2, (400, 0))
    pygame.display.flip()

pygame.quit()