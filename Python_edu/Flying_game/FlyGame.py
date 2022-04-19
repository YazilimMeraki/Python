import pygame
import tkinter

pygame.init()
# create window
Screen_width = 1000
Screen_height = 700
dic = "Fly_Game_File/Main_menu/"
menu_bg = pygame.image.load(dic + "menu_bg.png")
menu_bg = pygame.transform.scale(menu_bg, (1400, 900))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Flying Fighter Game")

# load button
start_btn = pygame.image.load(dic + "start.png").convert_alpha()
setting_btn = pygame.image.load(dic + "setting.png")
exit_btn = pygame.image.load(dic + "exit.png")

# Opening Song

pygame.mixer.music.load("Fly_Game_File/Sound/first-story.ogg")
pygame.mixer.music.play(-1)


# button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # check mouseover and clicked conditions
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


# create button instance

start_button = Button(350, 100, start_btn, 0.3)
setting_button = Button(345, 300, setting_btn, 0.3)
exit_button = Button(320, 500, exit_btn, 0.6)

# game loop
run = True


while run:

    screen.blit(menu_bg, (0, 0))

    if start_button.draw():


    if setting_button.draw():
        print("Setting")
    if exit_button.draw():
        run = False

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
