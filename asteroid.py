from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        split1_vector = self.velocity.rotate(random_angle)
        split2_vector = self.velocity.rotate(-random_angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split1 = Asteroid(self.position.x, self.position.y, split_radius)
        split2 = Asteroid(self.position.x, self.position.y, split_radius)

        split1.velocity = split1_vector * 1.2
        split2.velocity = split2_vector * 1.2