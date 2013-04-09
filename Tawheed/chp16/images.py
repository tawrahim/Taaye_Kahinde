import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("cat.jpg")
x = 50
y = 50
x_speed = 10
y_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "I am the event type and my name is", event.type
            sys.exit()
    
    pygame.time.delay(50)
    pygame.draw.rect(screen, [255,255,255], [x,y,150,90],0)
    x = x + x_speed
    y = y + y_speed
    # we do the (-90) because thats where we start
    if x > screen.get_width() - 90 or x < 0:
        x_speed = -x_speed
    if y > screen.get_height() -250 or y < 0:
        y_speed = -y_speed
    screen.blit(my_ball, [x,y])
    pygame.display.flip()


