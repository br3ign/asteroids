import circleshape
import pygame
import random
from contants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, 2)
        return super().draw(screen)   
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        new_ast_1 = Asteroid(self.position.x, self.position.y, radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, radius)

        new_ast_1.velocity = v1 * 1.2
        new_ast_2.velocity = v2 * 1.2
