import pygame, sys
pygame.init()

windowSize = (1003, 800)
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()