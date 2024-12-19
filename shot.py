import circleshape
import pygame
from contants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        self.radius = SHOT_RADIUS
        super().__init__(x, y, self.radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, SHOT_RADIUS)
        return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt