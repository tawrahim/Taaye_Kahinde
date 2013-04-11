# In step theree we are going to do a little
# bit more in our program by making the 
# ball move, thats pretty cool.. I think

import pygame
import sys
from random import *

class CoolGame():

    # lets create our init method, so that 
    # the user can pass in an image and location
    # We add a new parameter here called speed and
    # that is what is going to move the balls around
    def __init__(self, image_file, location, speed):
       self.image = pygame.image.load(image_file)
       self.rect = self.image.get_rect()
       
       # what ever the user gives us as a location 
       # we are going to add it to rectagular area 
       # of our image
       self.rect.left, self.rect.top = location
       self.speed = speed

    # lets create our move method
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
             self.speed[1] = -self.speed[1]

# Basic stuffs but the only difference 
# is we have multiple variable name on
# the same line, well we can do that :-)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
image_file = "beach_ball.png"

# Am going to create a list and then append
# multiple instances to it so that we can 
# loop through later
balls = []

for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-2,2]), choice([-2,2])]
        # Now, lets make an instance of our class
        game_obj = CoolGame(image_file, location,speed)
        # We append it to our balls list
        balls.append(game_obj)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Lets repaint the screeen after 20 seconds
    # remeber that it will run until the user stops
    # the window
    pygame.time.delay(20)
    screen.fill([255,255,255])
    for i in balls:
        # Remember that with every instance we want to
        # get the image and the location
        i.move()
        screen.blit(i.image, i.rect)
    pygame.display.flip()
