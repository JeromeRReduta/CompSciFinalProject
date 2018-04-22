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
            self.name = "Bun"
            self.img = pygame.image.load("resources/images/dude.png")
            self.rect = pygame.Rect(self.img.get_rect())

        def move(self):
            for pos in badguys:

                self.rect.top = pos[1]
                self.rect.left = pos[0]
                if pos[0] > 100 and pos[1] <= 100:
                    pos[0] -= 1
                if pos[0] <= 100 and pos[1] <= (height - 100):
                    pos[1] += 1
                if pos[1] >= (height - 100) and pos[0] < (width - 100):
                    pos[0] += 1
                if pos[0] >= (width - 100) and pos[1] > 100:
                    pos[1] -= 1

                # bad guy angle should be facing mouse
                badangle = math.atan2(position[1] - (pos[1] + 32), position[0] - (pos[0] + 26))
                rotation = pygame.transform.rotate(self.img, 360 - badangle * 57.29)
                badpos1 = (self.rect.left - rotation.get_rect().width / 2, self.rect.top - rotation.get_rect().height / 2)
                screen.blit(rotation, badpos1)




class Archer(Bunny):
        def __init__(self):
            super().__init__()

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



import random


# 2 - Initialize the game
pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
playerpos = [500, 500]

badguys = [[(width-100), 100]]


# 3 - Load images\
# Note: Rabbit and Badger images switched around = great results
player = pygame.image.load("resources/images/Navi (1).png")
badguyimg = pygame.image.load("resources/images/dude.png")
a = Bunny()
b = Bunny()
c = Bunny()
d = Bunny()
e = Bunny()

running = 1
exitcode = 0
while running:
    screen.fill(0)

    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))

    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    a.move()
    b.move()
    c.move()
    d.move()
    e.move()


    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
