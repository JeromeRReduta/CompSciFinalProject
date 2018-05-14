# Jerome Reduta

# Importing modules
import pygame
from pygame.locals import *
import math


class Player():
    def __init__(self):
        self.name = "Insert Name Here"
        self.img = pygame.image.load("resources\images/HeyListen.png")
        self.pos = [height/2, width/2]
        # Player tracks which direction (up, left, right, down) its moving independently of other dirctions
        self.keys = [False, False, False, False]
        self.rect = pygame.Rect(self.img.get_rect())

    # Checks to see if wasd held down, sets corresponding key to true
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
        # Moves player based on corresponding key
        if self.keys[0] and self.pos[1] >= 100:
            self.pos[1] -= 25
            self.rect.top -= 25
        elif self.keys[2] and self.pos[1] <= height-100:
            self.pos[1] += 25
            self.rect.top += 25
        if self.keys[1] and self.pos[0] >= 100:
            self.pos[0] -= 25
            self.rect.left -= 25
        elif self.keys[3] and self.pos[0] <= width-100:
            self.pos[0] += 25
            self.rect.left += 25
    # Blits fairy facing mouse
    def blit(self, mousepos):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        screen.blit(rot, self.pos)


class Bunny():
    def __init__(self, origin):
        self.name = "Bun"
        self.img = pygame.image.load("resources/images/dude.png")
        self.pos = origin
        self.direction = 3

    def move(self):
        # Sets direction of bunny when they hit a corner of screen
        if self.pos == [30, 40]:
            self.direction = 0
        if self.pos == [30, height-40]:
            self.direction = 1
        if self.pos == [(width-80), height-40]:
            self.direction = 2
        if self.pos == [(width-80), 40]:
            self.direction = 3
        movement = [1, 0, 1, 0]
        speed = [30, 30, -30, -30]
        # Moves bunny based on direction
        self.pos[movement[self.direction]] += speed[self.direction]

    # Blits bunny facing mouse
    def blit(self, mousepos):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        screen.blit(rot, self.pos)

    def shoot(self, mousepos, count):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        # Creates an arrow next to the bunny
        arrowList[count] = Arrow([self.pos[0]+1, self.pos[1] + 1], angle)
        # Adds arrow to arrows list
        arrows.append(arrowList[count])


class Arrow():
    def __init__(self, origin, angle):
        self.name = "Woody"
        self.img = pygame.image.load("resources/images/bullet.png")
        self.pos = origin
        self.angle = angle
        # Sets speed of arrow based on angle
        self.velx = math.cos(self.angle)*5
        self.vely = math.sin(self.angle)*5
        self.rect = pygame.Rect(self.img.get_rect())
        self.timer = 0

    def move(self):
        self.pos[0] += self.velx
        self.rect.left += self.velx
        self.pos[1] += self.vely
        self.rect.top += self.vely

    def blit(self):
        # Blits arrow facing direction bunny was facing when arrow "shot"/created
        arrow1 = pygame.transform.rotate(self.img, 360-self.angle*57.29)
        screen.blit(arrow1, self.pos)
        if self.pos[0] < 30 or self.pos[1] < 40 or self.pos[0] > width-80 or self.pos[1] > height-40:
            arrows.pop(0)
    def check(self):
        # Works too well atm - checks to see if arrow and player collide, reduces health if they do
        global healthvalue
        if b.rect.colliderect(self.rect) and self.timer == 0:
            print("ow!")
            healthvalue -= 1

# Start pygame
pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
grass = pygame.image.load("resources/images/grass.png")
# List to become 25 instances of bunnies
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
arrowList = []
entities = []
arrows = []
healthvalue = 5
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
timer = 30
c = 0
# Instantiate player
b = Player()

# Turns list of numbers into Bunny instances
for number in numbers:
    numbers[number] = Bunny([width+70, 40])

# Creates list of numbers in arrowList
x = 0

while x <= 100:
    arrowList.append(x)
    x += 1

# Stops bunnies from shooting arrows for 900 cycles
wait = 900

# Creates rapidfire pattern
rapidfiretimer = 2
# Stops bunnies from shooting (like shooting a volley, then stopping) for a while
cooldown = 0
u = 2
while True:
    wait -= 1
    timer -= 1
    print(wait)

    position = pygame.mouse.get_pos()
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(healthbar, (5, 5))
    for health1 in range(int(194 * healthvalue / 5)):
        screen.blit(health, (health1 + 8, 8))

    # 6 - draw the screen elements
    # 7 - update the screen
    if timer == 0:
        if wait >= 0:
            timer = 30
            if c < 25:
                # Spawns bunnies
                entities.append(numbers[c])
                c += 1
                print("There are " + str(c) + " bunnies")
                print("WAITING FOR " + str(wait) + " MORE FRAMES")
        if wait < 0:
            timer = 5
            if rapidfiretimer > 0:
                # Bunnies shoot volley
                for attacker in entities:
                    attacker.shoot(position, c)
                rapidfiretimer -= 1

            if rapidfiretimer == 0 and cooldown < 35:
                # Volley cooldown
               cooldown += 1

            if cooldown == 35:
                # Volley fires again
                rapidfiretimer = u
                cooldown = 0
                u += 1
            if c < 25:
                # Spawn bunnies
                entities.append(numbers[c])
                c += 1
                print("There are " + str(c) + " bunnies")
    # Enables player movement
    b.move()
    # Blits player
    b.blit(position)
    # Enables bunny movement, blits bunnies
    for enemy in entities:
        enemy.move()
        enemy.blit(position)
    # Arrow movement, blitting, checking if they hit player
    for shot in arrows:
        shot.move()
        shot.blit()
        shot.check()
    # Update screen
    pygame.display.flip()
    # 8 - loop through the events

    for thing in pygame.event.get():
        # check if the event is the X button
        if thing.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

