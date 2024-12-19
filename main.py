import pygame
import sys
from contants import *
import player as Player
from asteroid import *
from asteroidfield import *

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()

    Player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ast_field = AsteroidField()

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.display.set_caption("Asteroids")   

    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")

        for y in drawable:
            y.draw(screen)
        
        for x in updatable:
            x.update(dt)
        
        for z in asteroids:
            if z.collisions(player):
                game_running = False
                print("Game Over1")
                sys.exit()
            
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()