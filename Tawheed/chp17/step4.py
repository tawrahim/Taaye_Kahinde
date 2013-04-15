# In step four are going to do a little bit more
# by introducing collision detection in our program
# what that means is that we want to find out when 
# one ball hits the other, here we add the sprite object

import pygame
import sys
from random import *

class CoolGame(pygame.sprite.Sprite):

    # lets create our init method, so that 
    # the user can pass in an image and location
    # We add a new parameter here called speed and
    # that is what is going to move the balls around
    def __init__(self, image_file, location, speed):
       pygame.sprite.Sprite.__init__(self)
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


# method to animate the ball
def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        group.remove(ball)

        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)


# Basic stuffs but the only difference 
# is we have multiple variable name on
# the same line, well we can do that :-)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
image_file = "beach_ball.png"
group = pygame.sprite.Group()

for row in range(0,2):
    for column in range(0,2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-2,2]), choice([-2,2])]
        # Now, lets make an instance of our class
        game_obj = CoolGame(image_file, location,speed)
        # set our speed
        speed = [choice([-2,2]), choice([-2,2])]
        # We append it to our ball to the group
        group.add(game_obj)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animate(group)
