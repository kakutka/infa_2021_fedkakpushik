import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

text = pygame.font.Font(None, 36)
FPS = 2
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def click(event):
    return(x, y, r)

def smem(x, y, r, vx, vy):
    if x + r >= 1200:
        vx *= -1
    elif x - r <= 0:
        vx *= -1
    if y + r >= 900:
        vy *= -1
    elif y - r <= 0:
        vy *= -1
    return(vx, vy)

def ball(coopl):
    x, y, r, vx, vy, color = coopl
    x += vx
    y += vy
    circle(screen, color, (x, y), r)
    vx, vy = smem(x, y, r, vx, vy)
    coopl = (x, y, r, vx, vy, color)
    return coopl
    
def gener_ballxy():
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    coopl = (x, y, r, vx, vy, color)
    return coopl

def prov(coopl):
    x, y, r, vx, vy, color = coopl
    x2, y2 = event.pos
    if (x-x2)**2+(y-y2)**2<=r**2:
        return True
    return False

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k=0
coopl1 = gener_ballxy()
coopl2 = gener_ballxy()
coopl3 = gener_ballxy()
coopl4 = gener_ballxy()
coopl5 = gener_ballxy()

clock.tick(FPS)
sms = text.render("количество очков: " + str(k), True, (255, 255, 0))
screen.blit(sms, (0, 0))
pygame.display.update()
screen.fill(BLACK)
c = 0
g = 6
gh = [gener_ballxy() for i in range(g)]



while True:
    sms = text.render("количество очков: " + str(k), True, (255, 255, 0))
    clock.tick(40)
    for i in range(g):
        gh[i] = ball(gh[i])
    screen.blit(sms, (0, 0))
    pygame.display.update()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(g):
                    if prov(gh[i]):
                        gh[i] = (-100, -100, 1, 0, 0, (0, 0, 0))
                        k+= 1
                        c= 1
                        break

    if k == g:
        break
                        
        
        
    
    

pygame.quit()
