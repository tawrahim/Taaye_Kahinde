import pygame,sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([800,600])
screen.fill([255,255,240,255])
pygame.draw.rect(screen, [255,0,0],[400,400,50,90], 0)
pygame.display.flip()
pygame.time.delay(500)
#screen.fill([255,255,240,255])
pygame.draw.arc(screen, [255,0,0],[100,200,30,80], 90, 180,1)
pygame.display.flip()
while True:
    for tawheed in pygame.event.get():
        if tawheed.type == pygame.QUIT:
            sys.exit() 

