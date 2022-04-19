import pygame
from pygame import mixer
import random

pygame.init()

dic = "Characters/Sprites/"
class Enemy:
    def __init__(self):
        self.x = 1500
        self.y = random.randint(0, 1100)
        self.dx = random.randint(10, 50) / -10
        self.dy = random.randint(10, 50) / -10
        self.surface = pygame.image.load(dic+ "enemy.png")
        self.surface = pygame.transform.scale(self.surface, (200, 90))

    def explosive(self,enemy_xy,screen):
        self.surfaceE = pygame.image.load(dic + "explosive.png")
        self.surfaceE = pygame.transform.scale(self.surfaceE, (120, 50))
        screen.blit(self.surfaceE, (enemy_xy))

    def move(self):
        self.x = self.x + self.dx
        if self.x < 0:
            self.x = random.randint(1400, 1500)
            self.y = random.randint(0, 650)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))