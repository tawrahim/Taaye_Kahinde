import pygame, sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640, 640])
screen.fill([255, 255, 255])


pygame.draw.ellipse(screen, [255,0,0], [78,99,90,90], 0)
pygame.display.flip()
pygame.time.delay(50)
pygame.draw.arc(screen, THECOLORS['aliceblue'],[100,200,30,80], 90, 180,1)
pygame.display.flip() 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
