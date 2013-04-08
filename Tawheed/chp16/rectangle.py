import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.rect(screen, [255,0,0], [300,500,150,90],0)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print event.type
            sys.exit()
