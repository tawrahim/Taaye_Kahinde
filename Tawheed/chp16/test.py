import pygame,sys
pygame.init()
screen = pygame.display.set_mode([800,600])
screen.fill([255,255,240,255])
pygame.draw.circle(screen, [255,0,0],[100,100], 30, 0 )
pygame.display.flip()

while True:
    for tawheed in pygame.event.get():
        if tawheed.type == pygame.QUIT:
            sys.exit() 

