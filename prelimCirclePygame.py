import pygame
from PIL import Image
import os
im = Image.open("picture2.JPG")
im -im.convert('RGB')
pygame.init()
screen = pygame.display.set_mode([1000, 1000])
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    for x in range (0,100):
        for y in range (0,100):
            r,g,b = im.getpixel((x,y))
            pygame.draw.circle(screen, (r,g,b), (5+(x*10), 5+(y*10)), 5)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
