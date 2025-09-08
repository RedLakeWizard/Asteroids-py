import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import Asteroid
from shooting import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #infinite game loop
    while True:
        dt = clock.tick(60) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for i in drawable:
            i.draw(screen)
        
        for asteroid in asteroids:
            if player.collision(asteroid) == True:
                exit("Game over!")
            for bullet in shots:
                if bullet.collision(asteroid) == True:
                    bullet.kill()
                    asteroid.split()

        updatable.update(dt)
        
        player.player_cooldown = max(0.0, player.player_cooldown - dt)

        pygame.display.flip()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

