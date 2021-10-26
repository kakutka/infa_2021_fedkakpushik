import math
from random import choice
from random import randint as rnd
import pygame


RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball():
    def __init__(self, screen: pygame.Surface):
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.screen = screen
        self.live = 1
        self.color = (200, 200, 100)
        
    
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
    
    def testball(self, other):
        if (self.x-other.x)**2+(self.y-other.y)**2 <= (self.r + other.r)**2:
            self.color = (255, 0, 0)
            self.r = 30
            self.live = 0
            return True
        return False
            
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        
class Bugy_Vugy():
    def __init__(self, screen):
        self.x = rnd(100, 700)
        self.y = rnd(100, 300)
        self.vx = rnd(-5, 5)
        self.live = 1
        self.r = rnd(30, 50)
        self.color = GAME_COLORS[rnd(0, 5)]
        self.gun = 1000
        self.screen = screen
        
    def move(self):
        global gunball
        self.x += self.vx
        self.gun -= 5
        if self.x + self.vx >= 750:
            self.vx *= -1
        if self.x + self.vx <= 50:
            self.vx *= -1
        if self.live == 0:
            self.x = self.y = -100
            self.vx = 0
        if self.gun % 100 == 0:
            gg = Ball(self.screen)
            gg.x = self.x
            gg.y = self.y
            gg.color = (0, 200, 0)
            gg.vx = rnd(-4, 4)
            gg.vy = rnd(5, 10)
            gunball.append(gg)
            
    def test(self, other):
        if (self.x-other.x)**2+(self.y-other.y)**2 <= (self.r + other.r)**2:
            self.live = 0
            return True
        return False
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        

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
        self.x += self.vx
        if self.x + self.vx >= 750 or self.x+self.vx<=50:
            self.vx *= -1
    
    def draw(self):
        x = self.x
        y = self.y
        g = [(x-20, y+10), (x+20, y+10), (x+20,y), (x-20, y)]
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.polygon(self.screen, self.color, g)
    
    def test(self, other):
        if (self.x-other.x)**2+(self.y-other.y)**2 <= (self.r + other.r)**2:
            self.live = 0
            return True
        return False
    
    def gungun(self, event):
        global balls
        gun = Ball(self.screen)
        gun.r += 5
        self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        gun.vx = int(20 * math.cos(self.an))
        gun.vy = int(20 * math.sin(self.an))
        gun.x = self.x
        gun.y = self.y
        balls.append(gun)

        
        
        
        
        
            
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
gunball = []
balls = []
FPS = 30
clock = pygame.time.Clock()
bugy = Bugy_Vugy(screen)
tank = Tank(screen)
finished = False

while not finished:
    screen.fill((255, 255, 255))
    bugy.draw()
    tank.draw()
    for b in gunball:
        b.draw()       
    for bb in balls:
        bb.draw()
    pygame.display.update()
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            tank.gungun(event)
        #   gun.fire2_start(event)
        #elif event.type == pygame.MOUSEBUTTONUP:
        #    gun.fire2_end(event)
        #elif event.type == pygame.MOUSEMOTION:
        #    gun.targetting(event)

    for b in gunball:
        b.move()
        for bb in balls:
            b.testball(bb)
            bb.testball(b)
            if bugy.test(bb):
                bugy = Bugy_Vugy(screen)
        tank.test(b)
        
    for b in balls:
        b.move()
    bugy.move()
    if tank.move():
        f2 = pygame.font.Font(None, 50)
        text2 = f2.render("Вы проиграли", True, (0, 255, 0), (0, 0, 0))
        screen.blit(text2, (350, 280))               
        pygame.display.update()
        clock.tick(FPS)
        break
    

pygame.quit()
