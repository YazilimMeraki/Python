from Flying_game.Characters.Character import *


pygame.init()

player = Player()

dic = "Items/Item_Sprites/"


class Missile:
    def __init__(self):
        self.x = 0
        self.y = 1000
        self.dx = 0
        self.surface = pygame.image.load(dic + "missile.png")
        self.surface = pygame.transform.scale(self.surface, (100, 80))
        self.surface = pygame.transform.flip(self.surface, 200, 500)

    def fire(self, x, y):

        self.x = x + 25
        self.y = y + 25
        self.dx = 15

    def move(self):
        self.x = self.x + self.dx

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))



