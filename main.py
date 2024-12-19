import pygame
import sys
from contants import *
import player as Player
from asteroid import *
from asteroidfield import *
from shot import *

pygame.init()
pygame.font.init()

def main():
    player_score = 0
    lives = 3
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    game_clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

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
                print("Game Over!")
                sys.exit()
        
            for s in shots:
                if s.collisions(z):
                    player_score += 1
                    s.kill()
                    z.split()
        
        score_text = font.render(f'Score: {player_score}', True, (255, 255, 255))
        player_lives = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(player_lives, (SCREEN_WIDTH - 100, 10))
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()