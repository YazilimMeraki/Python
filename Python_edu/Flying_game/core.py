from Flying_game.Items.Missile import *
from Flying_game.Items.Enemy_Missile import *
from Characters.Character import *
from Characters.Enemy import *

pygame.init()

# screen attribute
WIDTH = 1000
HEIGHT = 700
# bg attribute
background = pygame.image.load("Core_Sprite/Cloud.png")
pygame.transform.scale(background, (700, 7000))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
bgX = 0
bgY = 0
# point and health
point = 0
health = 100
point_event = pygame.USEREVENT + 1
# icon
icon = pygame.image.load("Core_Sprite/red_01.png")
pygame.display.set_icon(icon)
# fps
clock = pygame.time.Clock()
# object call
player = Player()
enemy = Enemy()
missile = Missile()
e_missile = E_Missile()
# Pause
Is_pause = False
#
em_bullets = []
for ebul in range(1):
    em_bullets.append(e_missile)

enemies = []
for _ in range(6):
    enemies.append(Enemy())

bullets = []
for bul in range(1):
    bullets.append(Missile())
# sound
# bg sound
mixer.music.load("Core_Sound/battleground.ogg")
mixer.music.play(-1)

attack_sound = pygame.mixer.Sound("Core_Sound/converted_shot.wav")
explosive_sound = pygame.mixer.Sound("Core_Sound/converted_explosive.wav")


# score, health, pause

def score_text():
    font_score = pygame.font.SysFont("Ariel", 45)
    text_point = font_score.render("Score : " + str(point), True, (0, 0, 0))
    screen.blit(text_point, (0, 0))


x = 200
health_color = (0, 255, 0)


def health_text():
    health_txt = pygame.image.load("Core_Sprite/Text/Healt.png")
    health_txt = pygame.transform.scale(health_txt, (100, 50))
    screen.blit(health_txt, (1150, 0))

    health_bar = pygame.image.load("Core_Sprite/Text/Health-Bar.png")
    health_bar = pygame.transform.scale(health_bar, (x, 50))
    if x > 160:
        health_color = (0, 255, 0)
    elif x > 40:
        health_color = (255, 255, 0)
    else:
        health_color = (255, 0, 0)
    health_bar.fill(health_color)
    screen.blit(health_bar, (1100, 50))


def pause_text():
    font_pause = pygame.font.SysFont("Helvetica", 55)
    text_pause = font_pause.render(" PAUSED ", True, (255, 0, 0))
    screen.blit(text_pause, (1100, 650))


# main loop


run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_p:

                if Is_pause:
                    Is_pause = False
                else:
                    Is_pause = True
                    pause_text()

            if event.key == pygame.K_w:
                player.up()
            elif event.key == pygame.K_s:
                player.down()
            elif event.key == pygame.K_d:
                player.right()
            elif event.key == pygame.K_a:
                player.left()
            elif event.key == pygame.K_SPACE:
                attack_sound.play()
                missile.fire(player.x, player.y)

    if not Is_pause:
        player.move()
        missile.move()
        e_missile.EM_move()

        bgX -= 10

        if bgX == -1000:
            bgX = 1500
            bgY = random.randint(0, 500)

        screen.fill((0, 204, 255))
        screen.blit(background, (bgX, bgY))
        score_text()
        health_text()
        player.render(screen)
        for mis in bullets:
            missile.render(screen)
            missile.move()

        for em_bul in em_bullets:
            e_missile.render(screen)
            e_missile.EM_move()

        for enemy in enemies:
            enemy.move()

            enemy.render(screen)
            if enemy.distance(missile) < 90:
                point += 10
                enemy.x = random.randint(1400, 1500)
                enemy.y = random.randint(10, 650)

                explosive_sound.play()

                missile.dx = 0
                missile.x = 0
                missile.y = 1000
            if enemy.distance(player) < 100:
                x -= 20
                health -= 10
                enemy.x = random.randint(1400, 1500)
                enemy.y = random.randint(10, 750)
                if health == 0:
                    print("Game Over")
                    exit()

        pygame.display.flip()
    else:
        pygame.display.flip()
