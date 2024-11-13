import pygame
from constants import *

def main():
    pygame.init()

    running = True
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    while running: 

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        screen.fill([0,0,0])
        pygame.display.flip()
        print('Starting asteroids!')
        print(f'Screen width: {SCREEN_WIDTH}')
        print(f'Screen height: {SCREEN_HEIGHT}')


























if __name__ == "__main__":
    main()