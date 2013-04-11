import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
image = pygame.image.load("beach_ball.png")
screen.blit(image, [0,0])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

