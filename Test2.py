# Goals for Fri:
# 1: Fix this with classes
# 2: Play around with code - "break it"
# 2.5 Schedule what you want done and what can be done
# 3: Find way to make rabbits go around in circle
# 4: Find way to make rabbits shoot instead of badger when mouse clicked

# 1 - Import library
import pygame
from pygame.locals import *
import math



#Classes

class Bunny():
        def __init__(self):
            self.name = "yes"

        def move():
            if badguy[0] > 100 and badguy[1] <= 100:
                badguy[0] -= 20
            if badguy[0] <= 100 and badguy[1] <= (height - 100):
                badguy[1] += 20
            if badguy[1] >= (height - 100) and badguy[0] < (width - 100):
                badguy[0] += 20
            if badguy[0] >= (width - 100) and badguy[1] > 100:
                badguy[1] -= 20

class Archer(Bunny):
        def __init__(self):
            super().__init__(self)

        def shoot(self):
            badguys.append([0, 0])
            badtimer = 100 - (badtimer1 * 2)

            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)),
                 playerpos1[0] + 32,
                 playerpos1[1] + 32])
            badtimer = 100





# 2 - Initialize the game
pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []
badtimer = 7
badtimer1 = 0
badguys = [[(width-100), 100]]
healthvalue = 194

# 3 - Load images\
# Note: Rabbit and Badger images switched around = great results
player = pygame.image.load("resources/images/Navi (1).png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg = pygame.image.load("resources/images/dude.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
# 4 - keep looping through
running = 1
exitcode = 0
while running:
    badtimer -= 1
    # # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # "//" Is a floor divider (divides and takes greatest integer lower than result))
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (300, 300))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)


    # 6.2 - Draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < 20 or bullet[1] > (width-50) or bullet[2] < 20 or bullet[2] > (height-50):
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
        # 6.3 - Draw badgers
    if badtimer == 0:
        badguys.append([0,0])




    index = 0

    for badguy in badguys:

        Bunny.move()

        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        # bad guy angle should be facing mouse
        badguyrot = pygame.transform.rotate(badguyimg, 360 - angle * 57.29)
        badguypos1 = (badrect[0] - badguyrot.get_rect().width / 2, badrect[1] - badguyrot.get_rect().height / 2)
        screen.blit(badguyrot, badguypos1)
        # 6.4 - Draw clock
        font = pygame.font.Font(None, 24)


        # 6.3.1 - Attack castle

        # Commented out to test rectangular circuit movement
        # if badrect.left < 64:
        # healthvalue -= 20
        # badguys.pop(index)

        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1








    # 6.5 - Draw health bar
    screen.blit(healthbar, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 8, 8))

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
                 playerpos1[1] + 32])


    # 9 - Move player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

    # 10 - Win/Lose check
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0
# 11 - Win/lose display
# if exitcode == 0:
#     pygame.font.init()
#     font = pygame.font.Font(None, 24)
#     text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
#     textRect = text.get_rect()
#     textRect.centerx = screen.get_rect().centerx
#     textRect.centery = screen.get_rect().centery + 24
#     screen.blit(gameover, (0, 0))
#     screen.blit(text, textRect)
# else:
#     pygame.font.init()
#     font = pygame.font.Font(None, 24)
#     text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
#     textRect = text.get_rect()
#     textRect.centerx = screen.get_rect().centerx
#     textRect.centery = screen.get_rect().centery + 24
#     screen.blit(youwin, (0, 0))
#     screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

pygame.display.flip()

# Note: for screen

#screen = pygame.