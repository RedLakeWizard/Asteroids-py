import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        # sub-classes must override
         pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
       self.position += self.velocity * dt
