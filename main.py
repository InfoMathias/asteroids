import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids =  pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for member in updatable:
            member.update(dt)

        screen.fill('black')
        
        for member in drawable:
            member.draw(screen)

        for member in asteroids:
            if member.isColliding(player):
                print('Game Over') 
                return
            

        pygame.display.flip()

        dt = clock.tick(60) / 1000



























if __name__ == "__main__":
    main()