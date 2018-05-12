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
# class Player():
#     def __init__(self):
#         self.name = "Navi"
#         self.source = "http://zelda.wikia.com/wiki/Navi"
#         self.img = pygame.image.load("resources/images/Navi (1).png")
#         self.vel = 20
#         self.rect = pygame.Rect(self.img.get_rect())
#         self.pos = [100, 100]
#
#     def move(self):
#         # Turning the player to face mouse cursor
#         angle = math.atan2(position[1] - (self.rect.top + 32), position[0] - (self.rect.left + 26))
#         rotation = pygame.transform.rotate(self.img, 360 - angle * 57.29)
#         playerpos1 = (self.rect.left - rotation.get_rect().width / 2, self.rect.top - rotation.get_rect().height / 2)
#         # Showing the player on screen
#         screen.blit(rotation, playerpos1)
#         # Moving the player
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_w:
#                     keys[0] = True
#                 elif event.key == K_a:
#                     keys[1] = True
#                 elif event.key == K_s:
#                     keys[2] = True
#                 elif event.key == K_d:
#                     keys[3] = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_w:
#                     keys[0] = False
#                 elif event.key == pygame.K_a:
#                     keys[1] = False
#                 elif event.key == pygame.K_s:
#                     keys[2] = False
#                 elif event.key == pygame.K_d:
#                     keys[3] = False
#
#         if keys[0]:
#             self.rect.top -= self.vel
#             self.pos[1] -= self.vel
#         elif keys[2]:
#             self.rect.top += self.vel
#             self.pos[1] -= self.vel
#         if keys[1]:
#             self.rect.left -= self.vel
#             self.pos[0] -= self.vel
#         elif keys[3]:
#             self.rect.left += self.vel
#             self.pos[0] -= self.vel
#         print("Coordinates: " + str(self.pos))




# Enemy Class
class Bunny():
    def __init__(self):
        self.name = "Bun"
        self.img = pygame.image.load("resources/images/dude.png")
        self.rect = pygame.Rect(self.img.get_rect())
        self.origin = [100, 100]
        self.position = pygame.mouse.get_pos()
        # When self.timer hits 0, Bunny shoots an arrow

        self.arrowlist = []
        self.arrowsOnScreen = 0
        self.arrownames = ["a", "b", "c", "d", "e"]

        self.angle = math.atan2(self.position[1] - (self.origin[1] + 32), self.position[0] - (self.origin[0] + 26))
        self.rot = pygame.transform.rotate(self.img, 360 - self.angle * 57.29)
        self.pos1 = [self.rect.left - self.rot.get_rect().width / 2, self.rect.top - self.rot.get_rect().height / 2]
        self.timermax = 30
        self.timer = self.timermax


    # Looping movement of bunnies
    def move(self):
        if self.pos1[0] > 100 and self.pos1[1] <= 100:
            self.pos1[0] -= 25
        elif self.pos1[0] <= 100 and self.pos1[1] <= (height - 100):
            self.pos1[1] += 25
        elif self.pos1[1] >= (height - 100) and self.pos1[0] < width:
            self.pos1[0] += 25
        elif self.pos1[0] >= width and self.pos1[1] > 100:
            self.pos1[1] -= 25

    def blit(self):
        screen.blit(self.rot, self.pos1)

    def shoot(self):
        arrows.append(Arrow([self.pos1[0] + 1, self.pos1[1] + 1], 360 - self.angle * 57.29))

class Arrow():
    def __init__(self, origin, angle):
        self.name = "Woody"
        self.img = pygame.image.load("resources/images/bullet.png")
        self.rect = pygame.Rect(self.img.get_rect())
        self.origin = origin
        self.velx = 10*math.sin(angle)
        self.vely = 10*math.cos(angle)
        self.rot = pygame.transform.rotate(self.img, angle)
        self.pos1 = [self.rect.left - self.rot.get_rect().width / 2, self.rect.top - self.rot.get_rect().height / 2]


    def move(self):
        self.origin += [self.velx, self.vely]
        self.pos1[0] += self.velx
        self.pos1[1] += self.vely
        if self.origin[0] < 20 or self.origin[0] > (width - 50) or self.origin[1] < 20 or self.origin[1] > (height - 50):
            arrows.pop(0)
        print(self.pos1)
    def blit(self):
        screen.blit(self.rot, self.pos1)





#Note SOMETHING WRONG WITH POS1
pygame.init()
position = pygame.mouse.get_pos()
arrows = []
# Function that plays when player wins (all bunnies "withdraw") or loses (the player is hit 5 times)


# "2 - Initialize the game" - Julian Meyer, Ray Wenderlich

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

badtimermax = 30
badtimer = badtimermax
badguys = [[(width+200), 100]]


bunnies = []

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
for item in numbers:
    numbers[item] = Bunny()

# 3 - Load images\
# Note: Rabbit and Badger images switched around = great results
grass = pygame.image.load("resources/images/grass.png")
arrow = pygame.image.load("resources/images/bullet.png")


#Something wrong with pygame, reinstall it and look up "libpng warning: iCCCP: known incorrect sRGB profile"

# 4 - keep looping throu
# Can sustain ~ 464 bunnies
c = 1
t = 1

while True:
    badtimer -= 1
    # position = pygame.mouse.get_pos()
    # # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # "//" Is a floor divider (divides and takes greatest integer lower than result))
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))


    # 6.1 - Set player position and rotation

    if badtimer == 0:
        badtimer = badtimermax
        for enemy in bunnies:
            enemy.shoot()
        print("Shot " + str(len(arrows)))
        if c < 25:
            bunnies.append(numbers[c])
            c += 1
            print(str(c) + " bunnies present")
    for enemy in bunnies:
        enemy.move()
        enemy.blit()
    for shot in arrows:
        shot.move()
        shot.blit()

    # 7 - update the screen
    pygame.display.flip()

    # Research sprite collide




        # This code doesn't work anymore, but if I worked on it a bit longer it might enable a quit option

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         exit(0)


''' Current issues:
1) Arrows won't blit
2) Window keeps lagging, then crashing, not responding - try reintsalling pyGame, otherwise work from scratch
Note: IT'S NOT A PYGAME PROBLEM - SOMETHING WRONG WITH CODE - COMPAER TO WORKING VERS IN TEST5 AND FIND OUT WHY TI WON'T WORK'''

    # # 5 - clear the screen before drawing it again

    # 6 - draw the screen elements






        # This code doesn't work anymore, but if I worked on it a bit longer it might enable a quit option

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         exit(0)
