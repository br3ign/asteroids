import pygame
from contants import *
import player as Player

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.Player.containers = (updateable, drawable)

    player = Player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    pygame.display.set_caption("Asteroids")   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")

        for y in drawable:
            y.draw(screen)
        
        for x in updateable:
            x.update(dt)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()