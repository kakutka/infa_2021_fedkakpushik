import pygame
from pygame.draw import *
from random import randint
import math as m
pygame.init()
pygame.font.init()

text = pygame.font.Font(None, 36)
FPS = 2
screen = pygame.display.set_mode((1250, 950))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

person = input('Введите имя для начала игры: ')


"генерация координат и свойств объекта"
def gener_triangle():
    '''генерация координат правильного треугольника, его скорости поступательного движения, угола поворота, скорости вращения, длины стороны и скорости изменения стороны'''
    '''кортеж ssm нужен для изменения положения и свойств треугольника; он введен для того, чтобы не работать с глобальными переменными'''
    color = COLORS[randint(0, 5)]
    x = randint(200, 1000)
    y = randint(200, 700)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    da = randint(0, 360)
    da = 2 * 3.14 * da / 360
    lk = randint(40, 60)
    vlk = 2
    vda = 0.1
    ssm = (x, y, vx, vy, da, vda, lk, vlk, color)
    return ssm
"способность объекта отражаться и изменение свойств из-за отражения"
def reflaction(ssm):
    '''изменение скорости на противоположную при подлете к стене и случайное изменение направления вращения и скорости изменения размера'''
    x, y, vx, vy, da, vda, lk, vlk, color = ssm
    x1, y1 = (x, y)
    c = 0
    if x1 + vx > 1200:
        vx *= -1
        c = 1
    if y1 + vy > 900:
        vy *= -1
        c = 1
    if x1 + vx<50:
        vx *= -1
        c = 1
    if y1 + vy<50:
        vy *= -1
        c = 1
    if c==1:
        i = 1 if randint(10, 20) > 15 else -1
        vda *= i
        vlk *= i
    return(vx, vy, vda, vlk)
"создание объекта, рисовка"
def drowtiangle(ssm):
    '''данная функция рисует объект на экране по трем координатам, для нахождения которых используется модуль math'''
    x, y, vx, vy, da, vda, lk, vlk, color = ssm
    x += vx
    y += vy
    da += vda
    lk += vlk
    vx, vy, vda, vlk = reflaction(ssm)
    (x1, y1) = (x, y)
    (x2, y2) = (x+lk*m.cos(da), y-lk*m.sin(da))
    (x3, y3) = (x+lk*m.cos(1.04+da), y-lk*m.sin(1.04+da))
    coord = [(x1, y1), (x2, y2), (x3, y3)]
    ssm = (x, y, vx, vy, da, vda, lk, vlk, color)
    polygon(screen, color, coord)
    return ssm


def prov_popadania(ssm):
    '''данная функция проверяет, попал ли пользователь по объекту'''
    x, y, vx, vy, da, vda, lk, vlk, color = ssm
    (x1, y1) = (x, y)
    (x2, y2) = (x+lk*m.cos(da), y-lk*m.sin(da))
    (x3, y3) = (x+lk*m.cos(1.04+da), y-lk*m.sin(1.04+da))
    c1, c2 = event.pos
    minx, maxx = min(x1, x2, x3), max(x1, x2, x3)
    miny, maxy = min(y1, y2, y3), max(y1, y2, y3)
    if c1>minx and c1 <maxx and c2>miny and c2<maxy:
        return True
    return False
    
    
    
    




pygame.display.update()
clock = pygame.time.Clock()
finished = False
k=0


clock.tick(FPS)
sms = text.render("количество очков: " + str(k), True, (255, 255, 0))
screen.blit(sms, (0, 0))
pygame.display.update()
screen.fill(BLACK)
c = 0
gh = [gener_triangle() for i in range(randint(1, 20))]
g = len(gh)


while True:
    sms = text.render("количество очков: " + str(k), True, (255, 255, 0))
    clock.tick(40)
    for i in range(g):
        gh[i] = drowtiangle(gh[i])
    screen.blit(sms, (0, 0))
    pygame.display.update()
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(g):
                    if prov_popadania(gh[i]):
                        gh[i] = (-10, -10, 0, 0, 0, 0, 0, 0, (0,0,0))
                        k+=1
                        break
    if c==1:
        break

    if k == g:
        
        break
                        
        
        
text = pygame.font.Font(None, 100)  
sms = text.render("game over", True, (255, 255, 0))   
screen.blit(sms, (400, 200))
pygame.display.update()
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            clock.tick(400)
pygame.quit()
with open('ttt.txt', 'w') as d:
    b = 'Счёт игрока ' + person + ' равен ' + str(k) + '\n'
    d.write(b)
