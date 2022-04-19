import pygame
from pygame import mixer

pygame.init()


dic = "Characters/Sprites/"
class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dy = 0
        self.dx = 0
        self.surface = pygame.image.load(dic+ "Warplane.png")
        self.surface = pygame.transform.scale(self.surface, (200, 90))

    def up(self):
        self.dy = -4

    def down(self):
        self.dy = 4

    def left(self):
        self.dx = -4

    def right(self):
        self.dx = 4

    def move(self):
        self.y = self.y + self.dy
        self.x = self.x + self.dx

        if self.y < 0:
            self.y = 0
            self.dy = 0
        elif self.y > 650:
            self.y = 650
            self.dy = 0
        if self.x < 0:
            self.x = 0
            self.dx = 0
        elif self.x > 1350:
            self.x = 1350
            self.dx = 0

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
