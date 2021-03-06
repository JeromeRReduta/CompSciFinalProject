''' Goal: Remake game from scratch

Use .Group() class and .draw func (look up)'''

# Goal: Figure out how to make Player() move, add boundaries, music, arrows

# This version: "Dodge This"

import pygame
from pygame.locals import *
import math

# Goal: Make module for all my classes, funcs, etc.

class Player():
    def __init__(self):
        self.name = "Insert Name Here"
        self.img = pygame.image.load("resources\images/HeyListen.png")
        self.pos = [height/2, width/2]
        self.direction = 0
        self.keys = [False, False, False, False]

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    self.keys[0] = True
                elif event.key == K_a:
                    self.keys[1] = True
                elif event.key == K_s:
                    self.keys[2] = True
                elif event.key == K_d:
                    self.keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.keys[0] = False
                elif event.key == pygame.K_a:
                    self.keys[1] = False
                elif event.key == pygame.K_s:
                    self.keys[2] = False
                elif event.key == pygame.K_d:
                    self.keys[3] = False
        if self.keys[0]:
            self.pos[1] -= 25
        elif self.keys[2]:
            self.pos[1] += 25
        if self.keys[1]:
            self.pos[0] -= 25
        elif self.keys[3]:
            self.pos[0] += 25

    def blit(self, mousepos):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        screen.blit(rot, self.pos)


class Bunny():
    def __init__(self, origin):
        self.name = "Bun"
        self.img = pygame.image.load("resources/images/dude.png")
        self.pos = origin
        self.direction = 0

    def move(self):
        if self.pos == [100, 100]:
            self.direction = 0
        if self.pos == [100, (width-100)]:
            self.direction = 1
        if self.pos == [(width-100), (height-100)]:
            self.direction = 2
        if self.pos == [(width-100), 100]:
            self.direction = 3
        movement = [1, 0, 1, 0]
        speed = [25, 25, -25, -25]
        self.pos[movement[self.direction]] += speed[self.direction]

    def blit(self, mousepos):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        screen.blit(rot, self.pos)

    def shoot(self, mousepos, count):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = (360 - angle * 57.29)
        arrowList[count] = Arrow([self.pos[0]+1, self.pos[1] + 1], rot)
        arrows.append(arrowList[count])


class Arrow():
    def __init__(self, origin, rot):
        self.name = "Woody"
        self.img = pygame.image.load("resources/images/bullet.png")
        self.pos = origin
        self.angle = rot
        self.velx = math.cos(self.angle)
        self.vely = math.sin(self.angle)

    def move(self):
        self.pos[0] += self.velx
        self.pos[1] += self.vely

    def blit(self):
        for athing in entities:
            if athing.pos == self.pos:
                self.pos[0] += 5
                self.pos[1] += 5
        arrow1 = pygame.transform.rotate(self.img, self.angle)
        screen.blit(arrow1, self.pos)




pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
grass = pygame.image.load("resources/images/grass.png")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
arrowList = []
entities = []
arrows = []
# entities.append(Player())
timer = 30
c = 0

for number in numbers:
    numbers[number] = Bunny([100, 100])

x = 0
while x <= 100:
    arrowList.append(x)
    x += 1








while True:
    timer -= 1
    position = pygame.mouse.get_pos()
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    # 6 - draw the screen elements
    # 7 - update the screen
    if timer == 0:
        timer = 30
        if c < 25:
            entities.append(numbers[c])
            c += 1
            print("There are " + str(c) + " bunnies")


    for enemy in entities:
        enemy.move()
        enemy.blit(position)
        enemy.shoot(position, c)
        print(arrowList)
    for shot in arrows:
        shot.move()
        shot.blit()
    pygame.display.flip()
    # 8 - loop through the events
    for thing in pygame.event.get():
        # check if the event is the X button
        if thing.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

