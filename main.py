import pygame
from contants import *
import player


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")
        player1.update(dt)
        player1.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()