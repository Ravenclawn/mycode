import pygame,sys
from pygame.locals import *

RED=(255,0,100)
PURPLE=(200,0,200)
BLUE=(0,200,255)
BLACK=(0,0,0)

pygame.init()


surface=pygame.display.set_mode((640,480))
pygame.display.set_caption("ling")
font1=pygame.font.Font(None,100)
s=font1.render("4ever",True,RED)
rect=s.get_rect()
rect.center=(320,240)



while True:
  for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
        	print("KEYDOWN")
        elif event.type==KEYUP:
        	print("KEYUP")
        elif event.type==MOUSEMOTION:
        	mouse_x,mouse_y=event.pos
        	print("mm:%d,%d" %(mouse_x,mouse_y))
        	#fs=font.render("mm:"+str(mouse_x)+","+str(mouse_y),True,BLUE)
        elif event.type	==MOUSEBUTTONDOWN:
        	mouse_x,mouse_y=event.pos
        	print("md:%d,%d" %(mouse_x,mouse_y))
        elif event.type==MOUSEBUTTONUP:	
        	mouse_x,mouse_y=event.pos
        	print("mu:%d,%d" %(mouse_x,mouse_y))

  
  surface.fill((255,255,255))
  surface.blit(s,rect)
  #pygame.draw.circle(surface,RED,(320,240),200,1)
  #pygame.draw.line(surface,BLUE,(20,200),(100,200),20)
  #pygame.draw.polgon(surface,PURPLE,((123,0),(200,100),(189,339),(605,208)),10)---duobianxing
  #pygame.draw.ellipse(surface,BLUE,(30,50,200,60),10)------tuoyuan
  #pygame.drae.rect(surface,RED,(30,50,100,60))
  pygame.display.update()
  