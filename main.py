import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    running = True
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running: 

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False

        screen.fill([0,0,0])
        player.draw(screen)
        pygame.display.flip()
        # print('Starting asteroids!')
        # print(f'Screen width: {SCREEN_WIDTH}')
        # print(f'Screen height: {SCREEN_HEIGHT}')

        dt = clock.tick(60) / 1000


























if __name__ == "__main__":
    main()