import pygame,sys
import math

pygame.init()
screen = pygame.display.set_mode([800,600])
screen.fill([255,255,240,255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x,y])
pygame.draw.lines(screen, [0,0,0],False,plotPoints, 1)
pygame.display.flip()

while True:
    for tawheed in pygame.event.get():
        if tawheed.type == pygame.QUIT:
            sys.exit() 

