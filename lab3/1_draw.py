# let's give it a try

import math as m
import pygame
from pygame.draw import *

pygame.init()

FPS = 30

screen = pygame.display.set_mode((400, 400))
pygame.Surface.fill(screen, [127, 127, 127])

color = (255, 255, 0)
circle(screen, color, (200, 200), 100, 0)

color = (255, 0, 0)
circle(screen, color, (240, 180), 17, 0)
circle(screen, color, (160, 180), 20, 0)

color = (0, 0, 0)
circle(screen, color, (200, 200), 100, 1)
rect(screen, color, (152, 250, 100, 15), 0)
line(screen, color, (110, 110), (180, 160), 15)
line(screen, color, (220, 160), (290, 130), 15)
circle(screen, color, (240, 180), 9, 0)
circle(screen, color, (160, 180), 9, 0)
circle(screen, color, (240, 180), 17, 1)
circle(screen, color, (160, 180), 20, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
