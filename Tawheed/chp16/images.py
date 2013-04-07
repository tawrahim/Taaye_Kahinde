import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("cat.jpg")
screen.blit(my_ball, [50,50])
pygame.display.flip()
pygame.time.delay(2000)
pygame.draw.rect(screen, [255,255,255], [50,50,150,90],0)
screen.blit(my_ball, [300,50])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print event.type
            sys.exit()
