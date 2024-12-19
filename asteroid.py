import circleshape
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", (2,2), 2, 2)
        #return super().draw(screen)
    
    
    def update(self, dt):
        self.velocity = self.velocity * dt
        #return super().update(dt)