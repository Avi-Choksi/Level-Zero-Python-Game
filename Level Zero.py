import pygame
pygame.init()
from time import sleep
import time
import sys
import random
pygame.font.init()

win = pygame.display.set_mode ((640,400))

pygame.display.set_caption("Level Zero")

walkRight = [pygame.image.load('Images/R1.png'), pygame.image.load('Images/R2.png'), pygame.image.load('Images/R3.png'), pygame.image.load('Images/R4.png'), pygame.image.load('Images/R5.png'), pygame.image.load('Images/R6.png'), pygame.image.load('Images/R7.png'), pygame.image.load('Images/R8.png'), pygame.image.load('Images/R9.png')]
walkLeft = [pygame.image.load('Images/L1.png'), pygame.image.load('Images/L2.png'), pygame.image.load('Images/L3.png'), pygame.image.load('Images/L4.png'), pygame.image.load('Images/L5.png'), pygame.image.load('Images/L6.png'), pygame.image.load('Images/L7.png'), pygame.image.load('Images/L8.png'), pygame.image.load('Images/L9.png')]
bg = pygame.image.load('Images/background.png')
char = pygame.image.load('Images/standing.png')
el = pygame.image.load('Images/E1.png')
rect = pygame.Surface((640,400),pygame.SRCALPHA, 32)
Lv1 = pygame.image.load('Images/Lv1.png')
Lv2 = pygame.image.load('Images/Lv2.png')
Lv3 = pygame.image.load('Images/Lv3.png')
surface = pygame.Surface(Lv2.get_size(),depth=24)
key = (0,0,0,0)
#file = 'music.mp3'
file2 = 'OOF.mp3'
myfont = pygame.font.SysFont('rage',30)
fontgo = pygame.font.Font('Fonts/Pv.ttf',80)
fontm = pygame.font.Font('Fonts/Pv.ttf',50)
fontscore = pygame.font.Font('Fonts/RPGSystem.ttf',40)
INFO = pygame.image.load("Images/INFO2.png").convert_alpha()
INFO2 = pygame.image.load("Images/INFO.png").convert_alpha()
START = pygame.image.load("Images/START2.png").convert_alpha()
START2 = pygame.image.load("Images/START.png").convert_alpha()
LZ = pygame.image.load("Images/LZ.png").convert_alpha()

#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(file)
#pygame.mixer.music.play()
#pygame.event.wait()

def main():
    fontsmall = pygame.font.Font("Fonts/RPGSystem.ttf", 15)
    startscreen = pygame.image.load('Images/startscreen.png')
    clock = pygame.time.Clock()
    small = 'Created by Avi Choksi'
    start = True
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        win.blit(startscreen, (0,0))
        win.blit(LZ,(55,10))
        win.blit(START, (190,150))
        #win.blit (INFO,(220,250))
        if START.get_rect(center = (290,190)).collidepoint(pygame.mouse.get_pos()):
            win.blit(START2, (190,150))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if START.get_rect(center = (290,190)).collidepoint(mouse_pos):
                start = False
        #Info button, not in use
        #if INFO.get_rect(center = (320,310)).collidepoint(pygame.mouse.get_pos()):
        #    win.blit(INFO2, (220,250))
        txt_surfacesmall = fontsmall.render(small, True, pygame.Color('black'))
        win.blit(txt_surfacesmall, (10, 385))

        pygame.display.flip()
        clock.tick(30)

class player(object):
    def __init__(self,x,y,width,height): #Create definition for players
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17,self.y + 11,29,52)
        self.alive = True
        self.alpha = 5
        self.deaths = False
        self.game = -200
        self.over = 750
        self.score = 0
        self.r = False
        self.z = 0

    def draw(self,win): #Create definition for redrawing
        if not(self.alive):
            #gTrig = False
            #goblin.y = 450
            self.x = 300
            self.y = 275
            rect.fill((0, 0, 0, self.alpha))
            win.blit(rect, (0,0))
            if self.alpha > 245:
                txt_surfacegame = fontgo.render("GAME", True, pygame.Color('darkred'))
                win.blit(txt_surfacegame, (self.game, 50))
                if self.game < 150:
                    self.game += 50
                txt_surfaceover = fontgo.render("OVER", True, pygame.Color('darkred'))
                if self.over > 350:
                    self.over -= 50
                win.blit(txt_surfaceover, (self.over, 50))
                if self.over <= 350 and self.game >= 150:
                    txt_surfacescore = fontscore.render("Score: " "%d" % tuple([self.score]), True, pygame.Color('darkred'))
                    win.blit(txt_surfacescore, (270, 150))
                    if self.score < time:
                        self.score += 1
                    if self.score >= time:
                        txt_surfaceretry = fontm.render("RETRY", True, pygame.Color('darkred'))
                        win.blit(txt_surfaceretry, (120, 300))
                        if txt_surfaceretry.get_rect(center = (190,320)).collidepoint(pygame.mouse.get_pos()):
                            txt_surfaceretry2 = fontm.render("RETRY", True, pygame.Color('red'))
                            win.blit(txt_surfaceretry2, (120, 300))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            if txt_surfaceretry.get_rect(center = (190,320)).collidepoint(mouse_pos):
                                self.alive = True
                                run = True
                                self.r = True
                                restart()
                        txt_surfaceretry = fontm.render("Exit", True, pygame.Color('darkred'))
                        win.blit(txt_surfaceretry, (320, 300))
                        if txt_surfaceretry.get_rect(center = (390,320)).collidepoint(pygame.mouse.get_pos()):
                            txt_surfaceretry2 = fontm.render("Exit", True, pygame.Color('red'))
                            win.blit(txt_surfaceretry2, (320, 300))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            if txt_surfaceretry.get_rect(center = (390,320)).collidepoint(mouse_pos):
                                pygame.quit()
                                exit()

            #self.alive = True

        else:   
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//3],(self.x,self.y)) #Draw next image and move player left
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount//3],(self.x,self.y)) #Draw next image and move player right
                    self.walkCount += 1
            #If player is not moving face where they stopped
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x,self.y))
                else:
                    win.blit(walkLeft[0], (self.x,self.y))
        self.hitbox = (self.x + 17,self.y + 11,29,52)
        
class projectile(object):
    def __init__(self,x,y,radius,color,facing): #Create definition for projectiles
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self,win): #Create definition for redrawing
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class trigger(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 0
        self.hitbox = (self.x - 20,self.y,85,85)
        

    def draw(self,win):
        self.hitbox = (self.x - 60,self.y,100,100)
#        pygame.draw.rect(win, (255,0,0),self.hitbox,2)

class falling(object):
    def __init__(self,startx,endx,y,width,height):
        self.x = random.randint(startx,endx)
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = random.randint(5,15)
        self.hitbox = (self.x - 20,self.y,100,100)
        self.alive = True
        self.start = y
        

    def draw(self,win):
        if self.alive:
            win.blit(el,(self.x,self.y))
            self.hitbox = (self.x - 20,self.y,80,80)
#           pygame.draw.rect(win, (255,0,0),self.hitbox,2)
        else:
            self.y = self.start
            self.alive = True

class Saw(object):
    walkRight = [pygame.image.load('Images/S1.png'), pygame.image.load('Images/S2.png'), pygame.image.load('Images/S3.png'), pygame.image.load('Images/S4.png')]
    walkLeft = [pygame.image.load('Images/S1.png'), pygame.image.load('Images/S2.png'), pygame.image.load('Images/S3.png'), pygame.image.load('Images/S4.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 0
        self.hitbox = (self.x + 17,self.y + 2,31,57)
        

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//1],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//1],(self.x,self.y))
            self.walkCount +=1
        self.hitbox = (self.x - 35,self.y - 35,85,85)
            

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0

class gpower(object):
    walkRight = [pygame.image.load('Images/SP1.png'), pygame.image.load('Images/SP2.png'), pygame.image.load('Images/SP3.png'), pygame.image.load('Images/SP4.png')]
    walkLeft = [pygame.image.load('Images/SP1.png'), pygame.image.load('Images/SP2.png'), pygame.image.load('Images/SP3.png'), pygame.image.load('Images/SP4.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 0
        self.hitbox = (self.x,self.y + 2,31,57)
        

    def draw(self,win):
        if not(sGun) and pG:
            self.move()
            if self.walkCount + 1 >= 5:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//1],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//1],(self.x,self.y))
                self.walkCount +=1
            self.hitbox = (self.x - 30,self.y - 50,50,80)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        else:
            self.hitbox = (0,0,50,80)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0

class tpower(object):
    walkRight = [pygame.image.load('Images/T1.png'), pygame.image.load('Images/T2.png'), pygame.image.load('Images/T3.png'), pygame.image.load('Images/T4.png')]
    walkLeft = [pygame.image.load('Images/T1.png'), pygame.image.load('Images/T2.png'), pygame.image.load('Images/T3.png'), pygame.image.load('Images/T4.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 0
        self.hitbox = (self.x + 17,self.y + 2,31,57)
        

    def draw(self,win):
        if not(sTime) and pT:
            self.move()
            if self.walkCount + 1 >= 5:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//1],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//1],(self.x,self.y))
                self.walkCount +=1
            self.hitbox = (self.x - 30,self.y - 50,50,80)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)    
        else:
            self.hitbox = (0,0,50,80)
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0



class rockR(object):
    walkRight = [pygame.image.load('Images/B1.png'), pygame.image.load('Images/B2.png'), pygame.image.load('Images/B3.png'), pygame.image.load('Images/B4.png')]
    walkLeft = [pygame.image.load('Images/BR1.png'), pygame.image.load('Images/BR2.png'), pygame.image.load('Images/BR3.png'), pygame.image.load('Images/BR4.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17,self.y + 2,31,57)
        self.start = x
        self.alive = True

    def draw(self,win):
        if self.alive:
            self.move()
            if self.walkCount + 1 >= 8:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount +=1
            self.hitbox = (self.x - 50,self.y + 2,130,100)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        else:
            self.x = self.start
            self.hitbox = (0,0,130,100)
            self.alive = True

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0

    def hit(self):
        print('hit')

class fireBall(object):
    walkLeft = [pygame.image.load('Images/F1.png'), pygame.image.load('Images/F2.png'), pygame.image.load('Images/F3.png'), pygame.image.load('Images/F4.png'), pygame.image.load('Images/F5.png')]
    walkRight = [pygame.image.load('Images/FL1.png'), pygame.image.load('Images/FL2.png'), pygame.image.load('Images/FL3.png'), pygame.image.load('Images/FL4.png'), pygame.image.load('Images/FL5.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x,self.y,31,57)
        

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 8:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        self.hitbox = (self.x,self.y - 30,80,60)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkcount = 0

        
def restart():
    if man.r:
        man.z =  (pygame.time.get_ticks()-start_ticks)/1000
        man.r = False
    R1.x = -100
    R2.x = -100
    F1.x = -375
    F2.x = -375
    F3.x = -450
    F4.x = -375
    F5.x = -450
    F6.x = -375
    L2 = False
    L3 = False
    sGun = False
    ammo = 0
    alpha2 = 0
    alpha3 = 0
    alpha4= 255
    shootLoop = 0
    bullets = []
    run = True
    pG = False
    gTrig = False
    pT = False
    sTime = False
    sTimef = 0
    sTimet = 0

def mm():
    if man.r:
        man.z =  (pygame.time.get_ticks()-start_ticks)/1000
        man.r = False
    R1.x = -100
    R2.x = -100
    F1.x = -375
    F2.x = -375
    F3.x = -450
    F4.x = -375
    F5.x = -450
    F6.x = -375
    L2 = False
    L3 = False
    sGun = False
    ammo = 0
    alpha2 = 0
    alpha3 = 0
    alpha4= 255
    shootLoop = 0
    bullets = []
    run = True
    pG = False
    gTrig = False
    pT = False
    sTime = False
    sTimef = 0
    sTimet = 0
    start = True
    
def redrawGameWindow():
    win.blit(bg,(0,0)) #Redraw background
    surface.fill(key,surface.get_rect())
    surface.set_colorkey(key)
    surface.blit(Lv1,(0,0))
    surface.set_alpha(alpha4) 
    win.blit(surface,(150,50))
    textsurface = myfont.render("Time: " "%d" % tuple([time]), False, (0, 0, 0))
    win.blit(textsurface,(0,0))
    if L2:
        F3.draw(win)
        F4.draw(win)
        surface.fill(key,surface.get_rect())
        surface.set_colorkey(key)
        surface.blit(Lv2,(0,0))
        surface.set_alpha(alpha2) 
        win.blit(surface,(150,50))
    if L3:
        F5.draw(win)
        F6.draw(win)
        surface.fill(key,surface.get_rect())
        surface.set_colorkey(key)
        surface.blit(Lv3,(0,0))
        surface.set_alpha(alpha3) 
        win.blit(surface,(150,50))
    R1.draw(win)#Redraw goblin
    R2.draw(win)
    F1.draw(win)
    F2.draw(win)
    stime.draw(win)
    move.draw(win)
    #E1.draw(win)
    #E2.draw(win)
    #E3.draw(win)
    End.draw(win)
    gun.draw(win)
    for bullet in bullets: #Redraw projectile
        bullet.draw(win)
    man.draw(win)#Redraw player
    pygame.display.update()


#mainloop
rockd = random.randint (1,2)
man = player(300,275,64,64) #Set the x,y,width,and height for the object player
clockTick = 0
time = 0
R1 = rockR(-100,240,100,100,750)
R2 = rockR(-100,240,100,100,650)
F1 = fireBall(-375,60,100,100,750)
F2 = fireBall(-375,60,100,100,800)
F3 = fireBall(-450,100,100,100,750)
F4 = fireBall(-375,125,100,100,800)
F5 = fireBall(-450,160,100,100,750)
F6 = fireBall(-375,190,100,100,800)
E1 = falling(190,293,-150,80,107)
E2 = falling(293,396,-150,80,107)
E3 = falling(396,499,-150,80,107)
move = trigger(200,270,200,500)
End = trigger(30,400,10,500)
gun = gpower (random.randint(100,500),300,10,500,10)
stime = tpower (random.randint(100,500),300,10,500,10)
L2 = False
L3 = False
sGun = False
ammo = 0
alpha2 = 0
alpha3 = 0
alpha4= 255
shootLoop = 0
bullets = []
run = True
pG = False
gTrig = False
pT = False
sTime = False
sTimef = 0
sTimet = 0
start = True

main()

start_ticks=pygame.time.get_ticks()

while run:
    clock = pygame.time.Clock()
    clock.tick(27)
    if not (man.alive):
        if man.alpha < 255:
            man.alpha +=5
    if R1.x > 700:
        R1.x = -100
    if R2.x < -100:
        R2.x = 650
    if F1.x > 700:
        F1.x = -375
    if F2.x < -150:
        F2.x = 650
    if F3.x > 700:
        F3.x = -375
    if F4.x < -150:
        F4.x = 800
    if F5.x > 700:
        F5.x = -375
    if F6.x < -150:
        F6.x = 700
    if E1.y < 600:
        E1.y += E1.vel
    else:
        E1.alive = False
    if E2.y < 600:
        E2.y += E2.vel
    else:
        E2.alive = False
    if E3.y < 600:
        E3.y += E3.vel
    else:
        E3.alive = False
        
    if man.alive:
        time = (pygame.time.get_ticks()-start_ticks)/1000 - man.z
        if time < 1:
            L2 = False
            L3 = False
            sGun = False
            ammo = 0
            alpha2 = 0
            alpha3 = 0
            alpha4= 255
            shootLoop = 0
            bullets = []
            pG = False
            gTrig = False
            pT = False
            sTime = False
            sTimef = 0
            sTimet = 0
            R1.vel = 5
            R2.vel = 5
            man.vel = 5
            F1.vel = 5
            F2.vel = 5
            F3.vel = 5
            F4.vel = 5
            F5.vel = 5
            F6.vel = 5
            man.score = 0
    if alpha4 > 0:
        alpha4 -= 3
    if time > 15:
        R1.vel = 10
        R2.vel = 10
        man.vel = 10
        F1.vel = 10
        F2.vel = 10
    if time > 20:
        pG = True
    if time > 35:
        L2 = True
    if time >= 35 and time <= 40:
        alpha2 +=3
    else:
        if alpha2 > 0:
            alpha2 -= 3
    if time > 75:
        R1.vel = 20
        R2.vel = 20
        man.vel = 20
        F1.vel = 20
        F2.vel = 20
        F3.vel = 20
        F4.vel = 20
    if time > 95:
        L3 = True
    if time >= 115 and time <= 120:
        alpha3 +=3
    else:
        if alpha3 > 0:
            alpha3 -= 3
    if time > 155:
        R1.vel = 30
        R2.vel = 30
        man.vel = 30
        F1.vel = 30
        F2.vel = 30
        F3.vel = 30
        F4.vel = 30
        F5.vel = 30
        F6.vel = 30
    if time == random.randint(50,900):
        pG = True
    if time >= 75 and time == time + random.randint(0,25):
        pT = True

    if sTime:
        sTimef += 1
        if sTimef == 27:
            sTimef = 0
            sTimet += 1
        if sTimef < 108:
            R1.vel = (R1.vel / 2)
            R2.vel = (R2.vel / 2)
            F1.vel = (F1.vel / 2)
            F2.vel = (F2.vel / 2)
            F3.vel = (F3.vel / 2)
            F4.vel = (F4.vel / 2)
            F5.vel = (F5.vel / 2)
            F6.vel = (F6.vel / 2)
        if sTimet > 4:
            sTimet = 0
            if time >= 5:
                R1.vel = 10
                R2.vel = 10
                man.vel = 10
                F1.vel = 10
                F2.vel = 10
            if time >= 25:
                R1.vel = 20
                R2.vel = 20
                man.vel = 20
                F1.vel = 20
                F2.vel = 20
                F3.vel = 20
                F4.vel = 20
            if time >= 45:
                R1.vel = 30
                R2.vel = 30
                man.vel = 30
                F1.vel = 30
                F2.vel = 30
                F3.vel = 30
                F4.vel = 30
                F5.vel = 30
                F6.vel = 30
        
    #if not(man.alive):
        #gTrig = False
        #goblin.y = 450
    
    if man.y < E1.hitbox[1] + E1.hitbox[3] and man.y > E1.hitbox[1]:
        if man.x > E1.hitbox[0] and man.x < E1.hitbox[0] + E1.hitbox[2]:
            man.alive = False
            man.deaths = True
            #gTrig = False
            #goblin.y = 450
            
    if man.y < E2.hitbox[1] + E2.hitbox[3] and man.y > E2.hitbox[1]:
        if man.x > E2.hitbox[0] and man.x < E2.hitbox[0] + E2.hitbox[2]:
            man.alive = False
            man.deaths = True
            #gTrig = False
            #goblin.y = 450 

    if man.y < E3.hitbox[1] + E3.hitbox[3] and man.y > E3.hitbox[1]:
        if man.x > E3.hitbox[0] and man.x < E3.hitbox[0] + E3.hitbox[2]:
            man.alive = False
            man.deaths = True
            #gTrig = False
            #goblin.y = 450

    if man.y < R1.hitbox[1] + R1.hitbox[3] and man.y > R1.hitbox[1]:
        if man.x > R1.hitbox[0] and man.x < R1.hitbox[0] + R1.hitbox[2]:
            man.alive = False
            man.deaths = True
            #gTrig = False
            #goblin.y = 450
            
    if man.y < F1.hitbox[1] + F1.hitbox[3] and man.y > F1.hitbox[1]:
        if man.x > F1.hitbox[0] and man.x < F1.hitbox[0] + F1.hitbox[2]:
            man.alive = False
            man.deaths = True
    if man.y < F2.hitbox[1] + F2.hitbox[3] and man.y > F2.hitbox[1]:
        if man.x > F2.hitbox[0] and man.x < F2.hitbox[0] + F2.hitbox[2]:
            man.alive = False
            man.deaths = True

    if man.y < F3.hitbox[1] + F3.hitbox[3] and man.y > F3.hitbox[1]:
        if man.x > F3.hitbox[0] and man.x < F3.hitbox[0] + F3.hitbox[2]:
            man.alive = False
            man.deaths = True

    if man.y < F4.hitbox[1] + F4.hitbox[3] and man.y > F4.hitbox[1]:
        if man.x > F4.hitbox[0] and man.x < F4.hitbox[0] + F4.hitbox[2]:
            man.alive = False
            man.deaths = True
            
    if man.y < F5.hitbox[1] + F5.hitbox[3] and man.y > F5.hitbox[1]:
        if man.x > F5.hitbox[0] and man.x < F5.hitbox[0] + F5.hitbox[2]:
            man.alive = False
            man.deaths = True
            
    if man.y < F6.hitbox[1] + F6.hitbox[3] and man.y > F6.hitbox[1]:
        if man.x > F6.hitbox[0] and man.x < F6.hitbox[0] + F6.hitbox[2]:
            man.alive = False
            man.deaths = True

    if man.y < R2.hitbox[1] + R2.hitbox[3] and man.y > R2.hitbox[1]:
        if man.x > R2.hitbox[0] and man.x < R2.hitbox[0] + R2.hitbox[2]:
            man.alive = False
            man.deaths = True
            
    #if man.y < move.hitbox[1] + move.hitbox[3] and man.y > move.hitbox[1]:
        #if man.x > move.hitbox[0] and man.x < move.hitbox[0] + move.hitbox[2]:
            #gTrig = True

    if man.y < End.hitbox[1] + End.hitbox[3] and man.y > End.hitbox[1]:
        if man.x > End.hitbox[0] and man.x < End.hitbox[0] + End.hitbox[2]:
            #gTrig = False
            man.alive = False
            #goblin.y = 450
    if man.y < gun.hitbox[1] + gun.hitbox[3] and man.y > gun.hitbox[1]:
        if man.x > gun.hitbox[0] and man.x < gun.hitbox[0] + gun.hitbox[2]:
            sGun = True
    if man.y < stime.hitbox[1] + stime.hitbox[3] and man.y > stime.hitbox[1]:
        if man.x > stime.hitbox[0] and man.x < stime.hitbox[0] + stime.hitbox[2]:
            sTime = True
    #if gTrig and goblin.y > 260:
        #goblin.y -= 20
    #else:
        #gTrig = False
                
            
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get(): #Exit from game
        if event.type == pygame.QUIT:
            run = False
            
    for bullet in bullets:
        if bullet.y - bullet.radius < R1.hitbox[1] + R1.hitbox [3] and bullet.y + bullet.radius > R1.hitbox[1]:
            if bullet.x + bullet.radius > R1.hitbox[0] and bullet.x - bullet.radius < R1.hitbox[0] + R1.hitbox[2]:
                R1.alive = False
        if bullet.y - bullet.radius < R2.hitbox[1] + R2.hitbox [3] and bullet.y + bullet.radius > R2.hitbox[1]:
            if bullet.x + bullet.radius > R2.hitbox[0] and bullet.x - bullet.radius < R2.hitbox[0] + R2.hitbox[2]:
                R2.alive = False                
        if bullet.x < 640 and bullet.x > 0: #Set bullet boundary
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))#Remove bullet

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0 and sGun:
        if man.left: #Tells which way the player is facing
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5: #If less then 5 bullets on screen create projectile
            bullets.append(projectile(round(man.x + man.width //2), round(man.y+man.height//2),6,(0,0,0),facing))
        ammo += 1
        
        shootLoop = 1

    #if keys[pygame.K_ESCAPE]:
        

    if ammo > 2:
        sGun = False
        ammo = 0

    if keys[pygame.K_LEFT]and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT]and man.x < 640 - man.width -man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
    #Jump movement
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2)*0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    if man.y > 275:
        man.y = 275
        #gTrig = False
        #goblin.y = 450
    redrawGameWindow()

pygame.quit()

