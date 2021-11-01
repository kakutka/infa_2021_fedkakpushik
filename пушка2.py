#код для пушки2. пушка едет по земле, мишени(круг или квадрат) двигаются по всей плоскости и выпускают пули тоже

import math
from random import choice
from random import randint
import pygame
pygame.init()
pygame.font.init()

f1 = pygame.font.Font(None, 24)

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
#YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, GREEN, MAGENTA, CYAN]
GOLD = (255, 215, 0)

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 1

    ''''def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 5
        if self.x >= (800 - self.r) or self.x <= self.r :
            self.vx *= -1
            self.x += 2*self.vx
        if self.y >= (600 - self.r) or self.y <= self.r :
            self.vy *= -0.8
            '''
    def move(self):
        self.y += self.vy
        self.x += self.vx
        if self.live == 0:
            self.x = self.y = -100
            self.vx = self.vy = 0
        if self.x + self.vx >= 750:
            self.vx *= -1
        if self.x + self.vx <= 50:
            self.vx *= -1
        if self.y >= 600:
            self.color = (255, 0, 0)
            self.r = 30
            self.live = 0
    

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        x2, y2 = obj.x, obj.y
        if (self.x-x2)**2+(self.y-y2)**2<=(self.r+obj.r)**2:
            self.color = (255, 0, 0)
            self.r = 30
            self.live = 0
            return True
        return False

class Bugy_Vugy():
    def __init__(self, screen):
        self.x = randint(100, 700)
        self.y = randint(100, 300)
        self.vx = randint(-5, 5)
        self.vy = randint(-5,5)
        self.live = 1
        self.r = randint(30, 50)
        self.color = choice(GAME_COLORS)
        self.gun = 1000
        self.screen = screen
        
    def move(self):
        '''описывает движение стреляющей мишени'''
        global gunball
        self.x += self.vx
        self.y += self.vy
        self.gun -= 5
        if self.x + self.vx >= 750:
            self.vx *= -1
        if self.x + self.vx <= 50:
            self.vx *= -1
        if self.y + self.vy >= 550:
            self.vy *= -1
        if self.y + self.vy <= 50:
            self.vy *= -1
        if self.live == 0:
            self.x = self.y = -100
            self.vx = self.vy = 0
        if self.gun % 100 == 0:
            gg = Ball(self.screen)
            gg.x = self.x
            gg.y = self.y
            gg.color = (0, 200, 0)
            gg.vx = randint(-4, 4)
            gg.vy = randint(5, 10)
            gunball.append(gg)
            
    def test(self, obj):
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r + obj.r)**2:
            self.live = 0
            return True
        return False
        
    def draw(self):
        if randint(0,1):
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        else:
            x = self.x
            y = self.y
            r = self.r
            a = [(x-r, y-r), (x+r, y-r), (x+r, y+r), (x-r, y+r)]
            pygame.draw.polygon(self.screen, self.color, a)


class Tank():
    def __init__(self, screen):
        self.x = 100
        self.y = 580
        self.r = 10
        self.vx = 4
        self.live = 1
        self.color = (200, 0, 200)
        self.screen = screen
        
    def move(self):
        ''' описывает движение танка(по земле)'''
        self.x += self.vx
        if self.x + self.vx >= 750 or self.x+self.vx<=50:
            self.vx *= -1
        if self.live == 0:
            self.x = self.y = -100
            return True
        return False
    
    def draw(self):
        x = self.x
        y = self.y
        g = [(x-20, y+10), (x+20, y+10), (x+20,y), (x-20, y)]
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.polygon(self.screen, self.color, g)
    
    def test(self, obj):
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r*3 + obj.r)**2:
            self.live = 0
            return True
        return False
    
    def gungun(self, event):
        """Выстрел мячом. прицеливание

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet +=1
        gun = Ball(self.screen)
        gun.r += 5
        self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        gun.vx = int(20 * math.cos(self.an))
        gun.vy = int(20 * math.sin(self.an))
        gun.x = self.x
        gun.y = self.y
        balls.append(gun)
    



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
gunball = []

clock = pygame.time.Clock()
mis = Bugy_Vugy(screen)
tank = Tank(screen)
finished = False
count = 0


while not finished:
    screen.fill(WHITE)
    mis.draw()
    tank.draw()
    for b in gunball:
        if b.live >=1:
            b.draw()
    if tank.live>0:
        for bb in balls:
            if bb.live >=1:
                bb.draw()

    text2 = f1.render('Количество очков: '+str(count), True, (180,0,0))
    screen.blit(text2, (500, 50))
        
    pygame.display.update()

    
        
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tank.gungun(event)
           

    for b in gunball:
        b.move()
        if tank.live>0:
            for bb in balls:
                b.hittest(bb)
                bb.hittest(b)
                if mis.test(bb):
                    mis = Bugy_Vugy(screen)
                    count +=1
                tank.test(b)

    for b in balls:
        b.move()
    mis.move()
    if tank.move():
        text3 = f1.render('GAME OVER. YOU ARE LOSER. Ha-Ha-Ha', True, (180,0,0))
        screen.blit(text3, (200, 200))
        pygame.display.update()
        clock.tick(FPS)
        #break
        #если раскомментить брейк, то будет просто вылет из игры
    

pygame.quit()
