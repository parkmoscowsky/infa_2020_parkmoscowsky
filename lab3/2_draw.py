# first attempt

import pygame
from pygame.draw import *

pygame.init()

FPS = 30


def chukchi(surf, size, pos):
    color = (223, 223, 223)
    brown = (222, 188, 153)
    dark_brown = (167, 133, 106)
    light = (220, 208, 186)
    light_brown = (184, 151, 128)
    face = (214, 196, 194)
    black = (0, 0, 0)

    surface = pygame.Surface((0.05*size, 0.125*size))
    surface.fill(color)
    ellipse(surface, brown, (0, 0, 0.05*size, 0.125*size), 0)
    surface2 = pygame.transform.rotate(surface, 45)
    surf.blit(surface2, (pos[0] + 0.18*size, pos[1] + 0.37*size))

    circle(surf, light, (pos[0] + 0.15 * size, pos[1] + 0.25 * size), 0.1 * size, 0)
    ellipse(surf, brown, (pos[0] + 0.05*size, pos[1] + 0.25*size, 0.2*size, 0.75*size))
    ellipse(surf, brown, (pos[0], pos[1] + 0.4*size, 0.125 * size, 0.05 * size), 0)
    rect(surf, color, (pos[0] + 0.05*size, pos[1] + 0.625*size, 0.2*size, 0.375*size), 0)
    ellipse(surf, brown, (pos[0] + 0.08 * size, pos[1] + 0.58 * size, 0.05 * size, 0.12 * size), 0)
    ellipse(surf, brown, (pos[0] + 0.17 * size, pos[1] + 0.58 * size, 0.05 * size, 0.12 * size), 0)
    ellipse(surf, brown, (pos[0] + 0.04 * size, pos[1] + 0.68 * size, 0.08 * size, 0.03 * size), 0)
    ellipse(surf, brown, (pos[0] + 0.18 * size, pos[1] + 0.68 * size, 0.08 * size, 0.03 * size), 0)
    rect(surf, dark_brown, (pos[0] + 0.05 * size, pos[1] + 0.575 * size, 0.2 * size, 0.05 * size), 0)
    rect(surf, dark_brown, (pos[0] + 0.125 * size, pos[1] + 0.325 * size, 0.05 * size, 0.25 * size), 0)
    circle(surf, light_brown, (pos[0] + 0.15 * size, pos[1] + 0.25 * size), 0.075 * size, 0)
    circle(surf, face, (pos[0] + 0.15 * size, pos[1] + 0.25 * size), 0.05 * size, 0)
    aaline(surf, black, (pos[0], pos[1] + 0.2 * size), (pos[0] + 0.03 * size, pos[1] + 0.7 * size))
    aaline(surf, black, (pos[0] + 0.11 * size, pos[1] + 0.23 * size), (pos[0] + 0.13 * size, pos[1] + 0.24 * size))
    aaline(surf, black, (pos[0] + 0.16 * size, pos[1] + 0.24 * size), (pos[0] + 0.183 * size, pos[1] + 0.233 * size))
    arc(surf, black, (pos[0] + 0.12 * size, pos[1] + 0.27 * size, 0.06 * size, 0.04 * size), 0.5, 2.5)


def igloo(surf, size, pos):
    white = (255, 255, 255)
    black = (0, 0, 0)

    circle(surf, white, pos, size, 0, True, True)
    arc(surf, black, (pos[0] - size, pos[1] - size, 2 * size, 2 * size), 0, 3.17, 1)
    aaline(surf, black, (pos[0] - 0.75 * size, pos[1] - 0.66 * size), (pos[0] + 0.75 * size, pos[1] - 0.66 * size))
    aaline(surf, black, (pos[0], pos[1] - 0.66 * size), (pos[0], pos[1] - 0.33 * size))
    aaline(surf, black, (pos[0] - 0.94 * size, pos[1] - 0.33 * size), (pos[0] + 0.94 * size, pos[1] - 0.33 * size))
    aaline(surf, black, (pos[0] - 0.5 * size, pos[1] - 0.33 * size), (pos[0] - 0.5 * size, pos[1]))
    aaline(surf, black, (pos[0] + 0.5 * size, pos[1] - 0.33 * size), (pos[0] + 0.5 * size, pos[1]))
    aaline(surf, black, (pos[0] - size, pos[1]), (pos[0] + size, pos[1]))


def cat(surf, size, pos):
    gray = (127, 127, 127)
    dark_gray = (191, 191, 191)
    white = (255, 255, 255)
    black = (0, 0, 0)
    light = (223, 223, 223)

    surface = pygame.Surface((0.05 * size, 0.2 * size))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, 0.05 * size, 0.2 * size), 0)
    surface2 = pygame.transform.rotate(surface, -60)
    surf.blit(surface2, (pos[0] + 0.12 * size, pos[1] + 0.2 * size))

    surface = pygame.Surface((0.05 * size, 0.2 * size))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, 0.05 * size, 0.2 * size), 0)
    surface2 = pygame.transform.rotate(surface, -75)
    surf.blit(surface2, (pos[0], pos[1] + 0.15 * size))

    surface = pygame.Surface((0.07 * size, 0.28 * size))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, 0.07 * size, 0.28 * size), 0)
    surface2 = pygame.transform.rotate(surface, -60)
    surf.blit(surface2, (pos[0] + 0.7 * size, pos[1] - 0.05 * size))

    surface = pygame.Surface((0.05 * size, 0.2 * size))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, 0.05 * size, 0.2 * size), 0)
    surface2 = pygame.transform.rotate(surface, 60)
    surf.blit(surface2, (pos[0] + 0.6 * size, pos[1] + 0.2 * size))

    circle(surf, gray, (pos[0] + 0.18 * size, pos[1] + 0.06 * size), 0.08 * size, 0)
    circle(surf, white, (pos[0] + 0.16 * size, pos[1] + 0.04 * size), 0.015 * size, 0)
    circle(surf, white, (pos[0] + 0.20 * size, pos[1] + 0.05 * size), 0.015 * size, 0)
    circle(surf, black, (pos[0] + 0.165 * size, pos[1] + 0.04 * size), 0.005 * size, 0)
    circle(surf, black, (pos[0] + 0.205 * size, pos[1] + 0.05 * size), 0.005 * size, 0)
    polygon(surf, gray, ((pos[0] + 0.16 * size, pos[1] - 0.02 * size),
            (pos[0] + 0.19 * size, pos[1] - 0.05 * size),
            (pos[0] + 0.19 * size, pos[1] - 0.02 * size)), 0)
    polygon(surf, gray, ((pos[0] + 0.20 * size, pos[1] - 0.01 * size),
            (pos[0] + 0.23 * size, pos[1] - 0.04 * size),
            (pos[0] + 0.23 * size, pos[1])), 0)
    polygon(surf, black, ((pos[0] + 0.155 * size, pos[1] + 0.065 * size),
            (pos[0] + 0.175 * size, pos[1] + 0.065 * size),
            (pos[0] + 0.165 * size, pos[1] + 0.075 * size)), 0)

    surface = pygame.Surface((0.05 * size, 0.2 * size))
    surface.fill(light)
    ellipse(surface, gray, (0, 0, 0.05 * size, 0.2 * size), 0)
    surface2 = pygame.transform.rotate(surface, 75)
    surf.blit(surface2, (pos[0] + 0.7 * size, pos[1] + 0.15 * size))

    ellipse(surf, gray, (pos[0] + 0.12 * size, pos[1] + 0.08 * size, 0.66 * size, 0.15 * size), 0)

    polygon(surf, dark_gray, [(pos[0] + 0.09 * size, pos[1] + 0.06 * size),
            (pos[0] + 0.12 * size, pos[1] + 0.12 * size),
            (pos[0] + 0.22 * size, pos[1] + 0.16 * size),
            (pos[0] + 0.19 * size, pos[1] + 0.19 * size),
            (pos[0] + 0.15 * size, pos[1] + 0.09 * size)], 0)
    polygon(surf, black, [(pos[0] + 0.09 * size, pos[1] + 0.06 * size),
            (pos[0] + 0.12 * size, pos[1] + 0.12 * size),
            (pos[0] + 0.22 * size, pos[1] + 0.16 * size),
            (pos[0] + 0.19 * size, pos[1] + 0.19 * size),
            (pos[0] + 0.15 * size, pos[1] + 0.09 * size)], 1)

    polygon(surf, white, ((pos[0] + 0.13 * size, pos[1] + 0.08 * size),
                          (pos[0] + 0.14 * size, pos[1] + 0.08 * size),
                          (pos[0] + 0.13 * size, pos[1] + 0.11 * size)), 0)
    polygon(surf, white, ((pos[0] + 0.16 * size, pos[1] + 0.095 * size),
                          (pos[0] + 0.17 * size, pos[1] + 0.095 * size),
                          (pos[0] + 0.16 * size, pos[1] + 0.125 * size)), 0)


screen = pygame.display.set_mode((1024, 640))
screen.fill((255, 255, 255))
rect(screen, (223, 223, 223), (0, 320, 1024, 320), 0)

chukchi(screen, 500, (800, 200))
igloo(screen, 200, (300, 400))
cat(screen, 250, (300, 500))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
