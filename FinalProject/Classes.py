class Player():
    def __init__(self):
        self.name = "Insert Name Here"
        self.img = pygame.image.load("resources\images/HeyListen.png")
        self.pos = [height/2, width/2]
        self.keys = [False, False, False, False]
        self.rect = pygame.Rect(self.img.get_rect())


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
        self.pos[movement[self.direction]] += speed[self.direction]


    def blit(self, mousepos):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        rot = pygame.transform.rotate(self.img, 360 - angle * 57.29)
        screen.blit(rot, self.pos)

    def shoot(self, mousepos, count):
        angle = math.atan2(mousepos[1] - (self.pos[1] + 32), mousepos[0] - (self.pos[0] + 26))
        arrowList[count] = Arrow([self.pos[0]+1, self.pos[1] + 1], angle)
        arrows.append(arrowList[count])


class Arrow():
    def __init__(self, origin, angle):
        self.name = "Woody"
        self.img = pygame.image.load("resources/images/bullet.png")
        self.pos = origin
        self.angle = angle
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
        arrow1 = pygame.transform.rotate(self.img, 360-self.angle*57.29)
        screen.blit(arrow1, self.pos)
        if self.pos[0] < 30 or self.pos[1] < 40 or self.pos[0] > width-80 or self.pos[1] > height-40:
            arrows.pop(0)
    def check(self):
        global healthvalue
        if b.rect.colliderect(self.rect) and self.timer == 0:
            print("ow!")
            healthvalue -= 1
            self.timer = 100