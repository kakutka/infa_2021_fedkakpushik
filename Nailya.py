
import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((2000, 800))

line(screen, (175,238,238), (2000,200), (0,200), 400)
line(screen, (152,251,152), (2000,600), (0,600), 400)

ellipse(screen,(80, 80, 80), (300,250, 100, 275))
circle(screen,(245,245,220), (350,220), 40)
line(screen,(0,0,0), (320,280), (200, 420),1)
line(screen,(0,0,0), (380,280), (500, 420),1)

line(screen,(0,0,0), (320,490), (250, 650),1)
line(screen,(0,0,0), (250,650), (230, 650),1)
line(screen,(0,0,0), (380,490), (450, 650),1)
line(screen,(0,0,0), (450,650), (470, 650),1)


polygon(screen,(255,192,203), [(600,250), (660,525), (540,525)])
circle(screen,(245,245,220), (600,220), 40)
line(screen,(0,0,0), (605,280), (655, 370),1)
line(screen,(0,0,0), (655, 370),(690,280), 1)
line(screen,(0,0,0), (595,280), (500, 420),1)

line(screen,(0,0,0), (580,525), (530, 650),1)
line(screen,(0,0,0), (530,650), (510, 650),1)
line(screen,(0,0,0), (620,525), (670, 650),1)
line(screen,(0,0,0), (670,650), (690, 650),1)

line(screen,(0,0,0), (680, 340),(700,200), 1)
polygon(screen,(255,1,1), [(700,200), (740,170), (690,160)])
circle(screen,(255,1,1), (700,150), 20)
circle(screen,(255,1,1), (730,160), 20)

polygon(screen,(255,255,1), [(200,420), (200,380), (160, 380)])
circle(screen,(255,1,1), (190,370), 15)
circle(screen,(255,1,186), (170,380), 15)
circle(screen,(255,175,1), (180,360), 15)

#вторая пара
ellipse(screen,(80, 80, 80), (1300,250, 100, 275))
circle(screen,(245,245,220), (1350,220), 40)
line(screen,(0,0,0), (1320,280), (1200, 420),1)
line(screen,(0,0,0), (1380,280), (1500, 420),1)

line(screen,(0,0,0), (1320,490), (1250, 650),1)
line(screen,(0,0,0), (1250,650), (1230, 650),1)
line(screen,(0,0,0), (1380,490), (1450, 650),1)
line(screen,(0,0,0), (1450,650), (1470, 650),1)

#девочка 2
polygon(screen,(255,192,203), [(1000,250), (1060,525), (940,525)])
circle(screen,(245,245,220), (1000,220), 40)
line(screen,(0,0,0), (1005,280), (1200, 420),1)
line(screen,(0,0,0), (995, 280),(900, 380),1)
line(screen,(0,0,0), (900, 380), (700,300),1)

line(screen,(0,0,0), (980,525), (930, 650),1)
line(screen,(0,0,0), (930,650), (910, 650),1)
line(screen,(0,0,0), (1020,525), (1070, 650),1)
line(screen,(0,0,0), (1070,650), (1090, 650),1)


polygon(screen,(255,255,1), [(1500,420), (1500,360), (1540, 380)])
circle(screen,(255,1,1), (1510,370), 15)
circle(screen,(255,1,186), (1530,380), 15)
circle(screen,(255,175,1), (1520,360), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
