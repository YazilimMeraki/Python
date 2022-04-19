import random
import time
import pygame

dic = "Items/Item_Sprites/"

class E_Missile:
    def __init__(self):
        self.x = 0
        self.y = 1000
        self.dx = 0
        self.fire = False
        self.surface = pygame.image.load(dic + "missile.png")
        self.surface = pygame.transform.scale(self.surface, (50, 50))

    def EM_fire(self, x, y):
        a = random.randint(0, 2000)

        if a >= 1800:
            self.fire = True
            if self.fire == True:
                self.x = x + 25
                self.y = y + 25
                self.dx = -15
                self.fire==False
        else:
            self.fire == False

    def EM_move(self):
        self.x = self.x + self.dx

    def EM_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))