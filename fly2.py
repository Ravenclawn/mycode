import sys,random
import pygame
from pygame.locals import *
from os import path

img_dir="/home/cathy/test/images"
BLACK=(0,0,0)
PURPLE=(100,0,250)
FLY=(250)
BLUE=(0,0,250)
FPS=30

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,60))
        self.image.fill(PURPLE)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(480-30)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,8)
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top>700:
            self.rect.x=random.randrange(480-30)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,8)
mobs=[]
for i in range(8):
  m=Mob()
  mobs.append(m)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,40))
        self.image.fill(FLY)
        self.rect=self.image.get_rect()
        self.rect.centerx=240#SCREEN_WIDTH//2
        self.rect.bottom=690#SCREEN_HEIGHT-10
        self.speedx=0

    def update(self):
        self.rect.x+=self.speedx
        keys=pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.speedx=5
        elif keys[K_LEFT]:
            self.speedx=-5
        else:
            self.speedx=0
        self.rect.x+=self.speedx
        if self.rect.right>480:
            self.rect.right=480
        if self.rect.left<0:
            self.rect.left=0


pygame.init()
screen=pygame.display.set_mode((480,700))

bg=pygame.image.load(path.join(img_dir,'starfield.png')).convert()
bg_rect=bg.get_rect()
player_img=pygame.image.load(path.join(img_dir,'playerShip1_orange.png')).convert()
m_img=pygame.image.load(path.join(img_dir,'meteorBrown_med1.png')).convert()
bullet_img=pygame.image.load(path.join(img_dir,'laserRed16.png')).convert()

player=Player()
mob=Mob()
clock=pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
        	if event.key==K_LEFT:
        		player.speedx=-8
        	if event.key==K_RIGHT:
        		player.speedx=8 
    player.update()
    mob.update()
    screen.blit(bg)
    #for m in mobs:
    #    m.update()
    #screen.blit(bg)
    #for m in mobs:
    #    screen.blit(m_image)
    screen.blit(player_image)
    screen.blit(mob_image)
    pygame.display.flip()
