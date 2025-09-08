import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        new_vector_a = self.velocity.rotate(random_angle) 
        new_vector_b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_spawn_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_spawn_b = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_spawn_a.velocity = 1.2 * new_vector_a
        asteroid_spawn_b.velocity = 1.2 * new_vector_b
