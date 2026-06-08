import pygame
import random

#start pygame
pygame.init()

#Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 0)

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#caption of the window
pygame.display.set_caption("Sans")

class BoundingImage:
    def __init__(self, x, y, img, rd=False):
        self.img = pygame.image.load(img)
        self.img =pygame.transform.scale(self.img, (200,200))
        self.sans_rect = self.img.get_rect()
        self.x = x
        self.y = y
        self.direction = 1 + random.choice([-1, 1])
        self.speed_x = 3 + random.randint(2, 7)
        self.vel_y = 10 + random.randint(-2, 5)
        self.gravity = 0.5
        self.floor = 200

        self.rd = rd

        self.timer = 0
        self.change_interval = 60

    def tint(self):
        self.img.fill(color=(255,255,255), special_flags=pygame.BLEND_ADD)

    def random_move(self):
        self.timer += 1
        if self.timer > self.change_interval:
            self.timer = 0
            self.direction = random.choice([-1, 1])
            self.speed_x = random.randint(2, 7)
            self.change_interval = random.randint(30, 90)


    def move(self):

        if self.rd:
            self.random_move()

        self.x += self.speed_x * self.direction

        if self.x + self.img.get_width() >= SCREEN_WIDTH:
            self.direction = -1

        elif self.x <= 100:
            self.direction = 1

        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= self.floor:
            self.y = self.floor
            self.vel_y = -12

    def draw(self):
        SCREEN.blit(self.img, (self.x, self.y))


sans =  BoundingImage(100, 100, "sans.png", rd=False)
doggo = BoundingImage(400, 200, "doggo.png", rd=True)


#clock
clock = pygame.time.Clock()

#while loop for the run
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    SCREEN.fill(BACKGROUND_COLOR)

    sans.move()
    sans.draw()
    doggo.tint()
    doggo.move()
    doggo.draw()

    pygame.display.update()



pygame.quit()

