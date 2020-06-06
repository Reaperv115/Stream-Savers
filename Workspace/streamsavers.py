import pygame
import sys

pygame.init() #pylint: disable=maybe-no-member

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
black = 0, 0, 0

homer = pygame.image.load('C:\\Users\\rjs57\\gifs\\simpsons.gif') #pylint: disable=maybe-no-member
homerrect = homer.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pylint: disable=maybe-no-member
            sys.exit()
        screen.fill(black)
        screen.blit(homer, homerrect)
        pygame.display.flip()