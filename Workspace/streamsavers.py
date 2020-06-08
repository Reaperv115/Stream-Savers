from PIL import Image
from PIL import GifImagePlugin
import pygame
import sys

pygame.init() #pylint: disable=maybe-no-member

homer = pygame.image.open('C:\\Users\\rjs57\\gifs\\simpsons.gif', 'r')
homerrect = homer.get_rect()

size = width, height = homer.get_rect().x, homer.get_rect().y
screen = pygame.display.set_mode(homer.get_rect().size)
black = 0, 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pylint: disable=maybe-no-member
            running = False
        
        for frame in range(0, homer.n_frames):
            screen.fill(black)
            homer.seek(frame)
            screen.blit(homer, homerrect) #pylint: disable=maybe-no-member
            pygame.display.flip()

