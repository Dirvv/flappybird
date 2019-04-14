
import pygame
import random

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

# loading sounds
point = pygame.mixer.Sound('ding.mp3')
flap = pygame.mixer.Sound('')
dead = pygame.mixer.Sound('')

imageUp = pygame.image.load('birdwingsdown.png')
imageUp = pygame.transform.scale(imageUp, (40,40))

imageDown = pygame.image.load('birdwingsup.png')
imageDown = pygame.transform.scale(imageDown, (40,40))

imageDead = pygame.image.load('deadbird.png')
imageDead = pygame.transform.rotate(imageDead,180)
imageDead = pygame.transform.scale(imageDead, (40,40))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,0,255)
skyBlue = (0,191,255)
orange = (255,215,0)
gray = (112,138,144)

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

done = False
clock = pygame.time.Clock()

x = 350
y = 250

x_speed = 0
y_speed = 0

ground = 457
ceiling = 28
leftwall = 28
rightwall = 672

xloc = 700
yloc = 0
xsize = 70
ysize = random.randint(0,350)
space = 150
obspeed = 2.5
score = 0

# attempting to add music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)




def obstacles(xloc,yloc,xsize,ysize):
    imgTop = pygame.image.load('pipe.png')
    imgTop = pygame.transform.rotate(imgTop,180)
    imgTop = pygame.transform.scale(imgTop, (xsize,ysize))
    imgBottom = pygame.image.load('pipe.png')
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    screen.blit(imgTop, (xloc,yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))

def ball(x,y,image):
    screen.blit(image, (x,y))

def Score(score):
    font = pygame.font.SysFont(None,75)
    text = font.render("Score: " + str(score),True,black)
    screen.blit(text,[0,0])

# defining the high score and displaying it
def high_score(highScore):
    font = pygame.font.SysFont(None,30)
    text = font.render("High Score: " + str(highScore),True,black)
    screen.blit(text,[250,0])

# defining the splash screen
# code from sfjorge github
def splash_screen():
    splash = True
    while splash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                splash = False
            screen.fill(white)
            text = pygame.font.SysFont(None,75)
            text = font.render("Press any key to start.",True,gray)
            screen.bilt(text,50,300)
            pygame.display.update()
            clock.tick(40)

def gameover():
    font = pygame.font.SysFont(None,75)
    text = font.render("Game Over",True,red)
    screen.blit(text,[150,250])
    image = imageDead

image = imageUp

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            image = imageUp
            if event.key == pygame.K_UP:
                y_speed = -10
            if event.key == pygame.K_RIGHT:
                x_speed = 10
            if event.key == pygame.K_LEFT:
                x_speed = -10

        if event.type == pygame.KEYUP:
            image = imageDown
            if event.key == pygame.K_UP:
                y_speed = 3
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_LEFT:
                x_speed = 0

    screen.fill(skyBlue)



    obstacles(xloc,yloc,xsize,ysize)
    ball(x,y,image)
    Score(score)

    y += y_speed
    x += x_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0
        image = imageDead

    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 5
        image = imageDead

    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = 5
        image = imageDead

    if xloc < -80:
            xloc = 700
            ysize = random.randint(0,350)

    if x > xloc and x < xloc+3:
        score = (score + 1)

    if y < ceiling:
        y_speed = -(y_speed)
    if x < leftwall:
        x_speed = -(x_speed)
    if x > rightwall:
        x_speed = -(x_speed)
    if y > ground:
        gameover()
        y = ground
        image = imageDead

    pygame.display.flip()
    clock.tick(60)

pygame.quit()




