''' # Comp Sci Final Project
By Jerome Reduta
22 Apr. 2018 (#Punctual)
Unless otherwise mentioned, all sprites and many code structures from
    https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python'''

# Libraries
import pygame
from pygame.locals import *
import math

# Classes

# Player Class
class Player():
    def __init__(self):
        self.name = "Navi"
        self.source = "http://zelda.wikia.com/wiki/Navi"
        self.img = pygame.image.load("resources/images/Navi (1).png")
        self.vel = 20
        self.rect = pygame.Rect(self.img.get_rect())
        self.pos = [100, 100]

    def move(self):
        # Turning the player to face mouse cursor
        angle = math.atan2(position[1] - (self.rect.top + 32), position[0] - (self.rect.left + 26))
        rotation = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        playerpos1 = (self.rect.left - rotation.get_rect().width / 2, self.rect.top - rotation.get_rect().height / 2)
        # Showing the player on screen
        screen.blit(rotation, playerpos1)
        # Moving the player
        for event in pygame.event.get():
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

        if keys[0]:
            self.rect.top -= self.vel
            self.pos[1] -= self.vel
        elif keys[2]:
            self.rect.top += self.vel
            self.pos[1] -= self.vel
        if keys[1]:
            self.rect.left -= self.vel
            self.pos[0] -= self.vel
        elif keys[3]:
            self.rect.left += self.vel
            self.pos[0] -= self.vel
        print("Coordinates: " + str(self.pos))


# Enemy Class
class Bunny():
    def __init__(self):
        self.name = "Bun"
        self.img = pygame.image.load("resources/images/dude.png")
        self.rect = pygame.Rect(self.img.get_rect())
        self.origin = [100, 100]

        # When self.timer hits 0, Bunny shoots an arrow
        self.timeMax = 20
        self.timer = self.timeMax

        # I-frames, so Bunnies don't die from shooting their own arrow
        self.iFrames = 150

        # Tracks how many arrows missed by all bunnies (when arrows hit defined window boundary)
        # For every 5 arrows missed, a bunny "withdraws" (removed from game)
        self.miss = 0

        # When bunnies hit player, they get "freebie frames;" frames where arrows hitting defined window
        # boundary do not count as a miss
        self.freebiesMax = 180
        self.freebies = self.freebiesMax
        self.fairyIFrames = 100

    # Looping movement of bunnies
    def move(self):
        for pos in badguys:
            self.rect.top = pos[1]
            self.rect.left = pos[0]
            if pos[0] > 100 and pos[1] <= 100:
                pos[0] -= 25
            if pos[0] <= 100 and pos[1] <= (height - 100):
                pos[1] += 25
            if pos[1] >= (height - 100) and pos[0] < (width - 100):
                pos[0] += 25
            if pos[0] >= (width - 100) and pos[1] > 100:
                pos[1] -= 25

            # Bunnies face towards cursor
            badangle = math.atan2(position[1] - (pos[1] + 32), position[0] - (pos[0] + 26))
            rotation = pygame.transform.rotate(self.img, 360 - badangle * 57.29)

            badpos1 = (self.rect.left - rotation.get_rect().width / 2, self.rect.top - rotation.get_rect().height / 2)
            screen.blit(rotation, badpos1)
            self.timer -= 1
            self.freebies -= 1
            self.fairyIFrames -= 1
            print("Freebies left: " + str(self.freebies))
            print("fairyIFrames left: " + str(self.fairyIFrames))
            if self.timer == 0:
                self.iFrames = 10
                # Shooting an arrow
                acc[1] += 1
                arrows.append(
                    [math.atan2(position[1] - (badpos1[1] + 32), position[0] - (badpos1[0] + 26)), badpos1[0] + 32,
                     badpos1[1] + 32])
                self.timer = self.timeMax
                print (len(arrows))
        # Settings for arrows
        for bullet in arrows:
            velx = math.cos(bullet[0]) * 10
            vely = math.sin(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely
            # Defined window boundary for arrows
            if (bullet[1] < 20 or bullet[1] > (width - 50) or bullet[2] < 20 or bullet[2] > (height - 50)):
                arrows.pop(0)
                if self.freebies <= 0:
                    self.miss += 1
                    print("Missed: " + str(self.miss))
            # Showing arrows
            for projectile in arrows:
                arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
                screen.blit(arrow1, (projectile[1], projectile[2]))
                bullrect = pygame.Rect(arrow.get_rect())
                bullrect.left = bullet[1]
                bullrect.top = bullet[2]
                # Checking if player hit by arrows
                if b.rect.colliderect(bullrect):
                    print("ow!")
                    self.freebies = self.freebiesMax
                    if self.fairyIFrames <= 0:
                        global healthvalue
                        healthvalue -= 1
                        # lost.play()
                    self.fairyIFrames = 25
            if self.miss == 5:
                badguys.pop(0)
                print("Bunny withdrawn!")
                global c
                c -= 1
                self.miss = 0

# Function that plays when player wins (all bunnies "withdraw") or loses (the player is hit 5 times)


# "2 - Initialize the game" - Julian Meyer, Ray Wenderlich


pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []
badtimer = 25
badtimer1 = 0
badguys = [[(width+200), 100]]
healthvalue = 5
a = Bunny()
b = Player()

# 3 - Load images\
# Note: Rabbit and Badger images switched around = great results
grass = pygame.image.load("resources/images/grass.png")
arrow = pygame.image.load("resources/images/bullet.png")

# 4 - keep looping throu
# Can sustain ~ 464 bunnies
c = 1
t = 1
while True:
    badtimer -= 1
    # # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # "//" Is a floor divider (divides and takes greatest integer lower than result))
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()

    if badtimer == 0:
        badtimer = 25
        if c < 25 and t < 50:
            badguys.append([width+200, 100])
            c += 1
            t += 1
        print("Current # of Bunnies: " + str(c) + "/25")
        print("Total Bunnies Spawned: " + str(t) + "/50")
        print("------------------------------------------")

    a.move()
    b.move()


    # 7 - update the screen
    pygame.display.flip()

    # Research sprite collide