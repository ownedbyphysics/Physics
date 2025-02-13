import pygame

pygame.init()
img = pygame.image.load('jupiter.png')
pixel_color = img.get_at((50,50))  # Get the color of the top-left pixel
print(pixel_color)  # Check if it's really (0, 0, 0)