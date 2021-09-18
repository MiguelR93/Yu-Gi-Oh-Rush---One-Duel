import pygame, sys
pygame.init()

# my colours
WHITE = (255, 255, 255)

windowSize = (1003, 800)
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill(WHITE) # paints the screen

    pygame.display.flip() # actualizes the screen
    clock.tick(60) # frames per second

pygame.quit()