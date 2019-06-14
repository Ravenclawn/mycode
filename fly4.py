import sys,random
import pygame
from pygame.locals import *
from os import path

img_dir="/home/cathy/test/images"
snd_dir="/home/cathy/test/sound"

BLACK=(0,0,0)
PURPLE=(100,100,250)
FLY=(250,0,0)
BLUE=(0,0,250)
RED=(255,0,0)
YELLOW=(250,250,0)
WHITE=(250,250,250)
FPS=60

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_mob[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_mob[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_mob[self.size][self.frame]
                self.rect.center=center

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

            
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.orig_image=random.choice(m_images) 
        self.orig_image.set_colorkey(self.orig_image.get_at((0,0)))

        self.image=self.orig_image.copy()
        self.rect=self.image.get_rect()

        self.rect=self.image.get_rect()
         
        self.radius=int(self.rect.width*0.85//2)
        #pygame.draw.circle(self.image,BLUE,self.rect.center,self.radius)

        self.rect.x=random.randrange(480-30)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-4,4)
        self.rot=0

        self.rot_speed=random.randrange(-5,10)
        self.last_update=pygame.time.get_ticks()
    def rotate(self):
        now=pygame.time.get_ticks()
        if now - self.last_update >30:
            old_center=self.rect.center
            self.last_update=now
            self.rot=(self.rot+self.rot_speed)%360
            self.image=pygame.transform.rotate(self.orig_image,self.rot)
            self.rect.center=old_center

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top>710 or \
              self.rect.left < -25 or self.rect.right > 500:
            self.rect.x=random.randrange(480-30)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,8)
        self.rotate()
            
#mobs=[]
#for i in range(8):
 # m=Mob()
  #mobs.append(m)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,38))
        self.image=player_img
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*0.7//2)
        #pygame.draw.circle(self.image,BLUE,self.rect.center,self.radius)

        self.rect.centerx=240#SCREEN_WIDTH//2
        self.rect.bottom=690#SCREEN_HEIGHT-10
        self.speedx=0
        self.shield=100

        self.shoot_delay=200

        self.lives=3
        self.hidden=False
        self.hide_timer=pygame.time.get_ticks()

    def hide(self):
        self.hidden=True
        self.hide_timer=pygame.time.get_ticks()
        self.rect.center=(240,650)

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
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_snd.play()


font_name=pygame.font.match_font('French Script')

def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    SUR=font.render(text,True,WHITE)
    rect=SUR.get_rect()
    rect.midtop=(x,y)
    surf.blit(SUR,rect)
def draw_shield_bar(surf,pt,x,y):
    if pt<0:
        pt=0
    WIDTH=100
    HEIGHT=10
    fill=(pt/100)*WIDTH
    outline_rect=pygame.Rect(x,y,WIDTH,HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,HEIGHT)
    pygame.draw.rect(surf,RED,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)
def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        rect=img.get_rect()
        rect.x=x+30*i
        rect.y=y
        surf.blit(img,rect)

pygame.init()
screen=pygame.display.set_mode((480,700))

bg=pygame.image.load(path.join(img_dir,'starfield.png')).convert()
bg=pygame.transform.scale(bg,(480,700))
bg_rect=bg.get_rect()
player_img=pygame.image.load(path.join(img_dir,'playerShip1_orange.png')).convert()

player_img_mini=pygame.transform.scale(player_img,(25,19))
player_img_mini.set_colorkey(player_img_mini.get_at((0,0)))

m_images=[]
m_list=["meteorBrown_big2.png","meteorBrown_big2.png","meteorBrown_med1.png","meteorBrown_med3.png","meteorBrown_small1.png","meteorBrown_tiny1.png","meteorBrown_tiny2.png"]

for x in m_list:
    img=pygame.image.load(path.join(img_dir,x)).convert()
    m_images.append(img)

shoot_snd=pygame.mixer.Sound(path.join(snd_dir,"pew.wav"))
explode_sounds=[]
for s in['expl3.wav','expl6.wav']:
    snd=pygame.mixer.Sound(path.join(snd_dir,s))
    explode_sounds.append(snd)
bk_snd=pygame.mixer.Sound(path.join(snd_dir,"tgfcoder-FrozenJam-SeamlessLoop.ogg"))



bullet_img=pygame.image.load(path.join(img_dir,'laserRed16.png')).convert()
all_sprites=pygame.sprite.Group()
mobs=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
bk_snd.play(-1)

#def func_c(r1,r2):
#    if r1.left>r2.right or r1.right<r2.left:
#        return False
#    if r1.top>r2.bottom or r1.bottom<r2.top:
#        return False
#    return True;
#ms=[]
explosion_mob={}
explosion_mob['lg']=[]
explosion_mob['sm']=[]
explosion_mob['player']=[]
for i in range(9):
    filename='regularExplosion0{}.png'.format(i)
    img=pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(img.get_at((0,0)))
    img_lg=pygame.transform.scale(img,(75,75))
    explosion_mob['lg'].append(img_lg)
    img_sm=pygame.transform.scale(img,(32,32))
    explosion_mob['sm'].append(img_sm)
    filename_pl='sonicExplosion0{}.png'.format(i)
    img_pl=pygame.image.load(path.join(img_dir,filename_pl)).convert()
    img_pl.set_colorkey(img.get_at((0,0)))
    explosion_mob['player'].append(img_pl)
for i in range(10):
  m=Mob()
  all_sprites.add(m)
  mobs.add(m)
#  ms.append(m)  

clock=pygame.time.Clock()

play_scores=0

running=True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                player.speedx=-8
            elif event.key==K_RIGHT:
                player.speedx=8 
            elif event.key==K_SPACE:
                player.shoot()

                

    #screen.blit(bg)
    all_sprites.update()
    hits=pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)
    for m in hits:
        player.shield-=m.radius//2
        expl=Explosion(m.rect.center,'lg')
        all_sprites.add(expl)

        newm=Mob()
        all_sprites.add(newm)
        mobs.add(newm)

        if player.shield<=0:
            death_explosion=Explosion(player.rect.center,'player')
            all_sprites.add(death_explosion)
            #running=False
            player.hide()
            player.lives-=1
            player.shield=100
        if player.lives==0 and not death_explosion.alive():
            running=False


    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        snd=random.choice(explode_sounds)
        expl=Explosion(hit.rect.center,'lg')
        all_sprites.add(expl)
        snd.play()
        
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)
        
        play_scores+=100-hit.radius



#    for m in ms:
#        if func_c(m.rect,player.rect)==True:
#            print("a-oh!")
#            sys.exit()
    
    screen.fill(BLACK)
    screen.blit(bg,bg_rect)
    all_sprites.draw(screen)
    draw_text(screen,str(play_scores),18,240,10)
    draw_shield_bar(screen,player.shield,5,5)
    draw_lives(screen,300,5,player.lives,player_img_mini)
    pygame.display.flip()