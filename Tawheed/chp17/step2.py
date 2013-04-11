# In step two we are going to learn how
# we can put our code into a class and 
# not repeat ourselves, lets keep it DRY!

import pygame, sys

class CoolGame():

    # lets create our init method, so that 
    # the user can pass in an image and location
    def __init__(self, image_file, location):
       self.image = pygame.image.load(image_file)
       self.rect = self.image.get_rect()
       
       # what ever the user gives us as a location 
       # we are going to add it to rectagular area 
       # of our image
       self.rect.left, self.rect.top = location


size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

image_file = "beach_ball.png"
location = [100, 100]

# Now, lets make an instance of our class
game_obj = CoolGame(image_file, location)
screen.blit(game_obj.image, game_obj.rect)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

