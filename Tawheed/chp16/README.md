## Some basics that you nedd when creating a pygame program
These are some basic steps that you would like to have in your program no matter what game you are creating

```
This line imports the pygame module
* import pygame

Initialize pygame (Telling the pygame module that you need it!)
* pygame.init()

We need to set the size of the window to display our game, (also save to a variable called screen, you can use any variable you 
want I just chose screen), feel free to change the window size
* screen = pygame.display.set_mode([640, 480])

We need to fill the screen (paint the background some colour) I chose to use white which is 255,255,255. Feel free to use what you like
* screen.fill([255, 255, 255])

//Now the rest of your program comes here, whatever you choose to do in your program is up to you!


Once we are done, we need this to properly display our game. omit it and I bet you that it wont work
* pygame.display.flip()
