page = 'c:\Users\lenovo pc\desktop\imgs\page.png'
failpic = 'c:\Users\lenovo pc\desktop\imgs\lpage.png'
import random,pygame
from pygame import *
score = 0
class wall(object):
    def __init__(self):
        self.x=640.0
        self.y1=random.randint(75,275)+0.0
        self.y2=self.y1+100.0
        self.speed = 0
green = (55,239,80)
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
xp=0
yp=0
flag = 0
screen.fill((120,120,120))
font = pygame.font.Font(None,93)
firstpage = pygame.image.load(page).convert()
fail = pygame.image.load(failpic).convert_alpha()

while True:
    xp = 0
    yp = 0
    screen.blit(firstpage,(0,0))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            (xp , yp) = pygame.mouse.get_pos()
        if event.type == QUIT:
            exit()
    if ((xp>184 and xp<464) and (yp>133 and yp<229)):
        flag = 1
    if((xp>186 and xp< 464) and (yp>301 and yp<398)):
        exit()
    if flag == 1:
        break
    pygame.display.update()

srik = wall()
s=wall()
t=wall()
srik.speed= 120.0
x=320.0
y=240.0
g=350.0
v=0.0
ti=0.0
time=0.0
clock = pygame.time.Clock()
pink = (100,20,200)
font = pygame.font.Font(None,40)

while True:
    v += g * ti
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            v=-200
    if ((y >= 460) or (y <= 0)):
        for xyz in pygame.event.get():
            exit()
            

        
    srik.x = srik.x - srik.speed*ti
    s.x = s.x - s.speed*ti
    t.x = t.x - t.speed*ti
    ti=clock.tick(60)/1000.0
    y +=( v * ti + 1/2 * g * ti * ti)
    time+=ti
    if time>=3 :
        s.speed = 120.0
    if time>= 6 :
        t.speed = 120.0

    if srik.x < -20:
        srik = wall()
    if s.x < -20:
        s = wall()
    if t.x < -20:
        t = wall()
    if ((t.x <= 315 and t.x >= 313)or(srik.x <= 315 and srik.x >= 313)or(s.x <= 315 and s.x >=313)) :
        score = score + 1

    screen.fill((0,0,0))
    text = font.render('score :',1,(220,220,220))
    scr = font.render((str)(score),1,(255,255,255))
    
    
    pygame.draw.rect(screen,pink,(x,y,20,20),3)
    pygame.draw.rect(screen,green,(srik.x,0,20,srik.y1),0)
    pygame.draw.rect(screen,green,(srik.x,srik.y2,20,480),0)
    pygame.draw.rect(screen,green,(s.x,0,20,s.y1),0)
    pygame.draw.rect(screen,green,(s.x,s.y2,20,480),0)
    pygame.draw.rect(screen,green,(t.x,0,20,t.y1),0)
    pygame.draw.rect(screen,green,(t.x,t.y2,20,480),0)
    screen.blit(text,(25,25))
    screen.blit(scr,(120,25))
    pygame.display.update()


