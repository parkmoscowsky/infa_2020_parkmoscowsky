# THE BEST 6TH DORM SIMULATOR OF 2020

import pygame
from pygame.draw import *
from random import randint
import math as m

pygame.init()

# defining variables for counting aim and list for cockroaches' parameters
i = 0
cockroaches = []

# setting FPS, timer & screen color
FPS = 30
timer = 1800
WHITE = (255, 255, 255)

# creating the screen
screen = pygame.display.set_mode((900, 900))
screen.fill(WHITE)


# defining way too many functions
def draw_screen(t):
    '''
    function draws the screen for showing the time left
    :param t: remaining time
    :return: colored pygame screen
    '''
    color_change = int(224 * t / 1800)
    screen_color = (255 - color_change, 31 + color_change, 31)
    screen.fill(WHITE)
    rect(screen, screen_color, (0, 0, t / 2, 900), 0)


def draw_cockroach():
    '''
    the function creates an image of a cockroach
    :return: pygame surface with the image
    '''
    surf = pygame.Surface((50, 50))
    surf.fill((255, 255, 255))
    ellipse(surf, (255, 160, 122), (0, 15, 40, 20), 0)
    ellipse(surf, (160, 82, 45), (10, 18, 30, 14), 0)
    paw_positions = (((10, 15), (10, 8), (0, 5)), ((20, 15), (20, 8), (10, 5)),
                     ((30, 15), (30, 8), (20, 5)), ((10, 35), (10, 42), (0, 45)),
                     ((20, 35), (20, 42), (10, 45)), ((30, 35), (30, 42), (20, 45)),
                     ((35, 20), (40, 18), (50, 5)), ((35, 30), (40, 32), (50, 45)))
    for paw in paw_positions:
        lines(surf, (139, 69, 19), False, paw)
    return surf


def cockroach(size, x, y, vx, vy):
    '''
    the function rotates the image of a cockroach and changes its scale
    :param size: the size of the final picture in pixels / 50
    :param x: x coordinate of the centre of a cockroach
    :param y: y coordinate of the centre of a cockroach
    :param vx: x coordinate of the velocity of a cockroach
    :param vy: y coordinate of the velocity of a cockroach
    :return: the picture of given size of a cockroach heading along its velocity
    '''
    surface2 = pygame.transform.rotate(surface, - 180 * m.atan2(vy, vx) / m.pi)
    surface3 = pygame.transform.scale(surface2, (int(screen.get_width() * size), int(screen.get_height() * size)))
    screen.blit(surface3, (x - 500 * size, y - 500 * size))


def new_cockroach():
    '''
    the function creates a new cockroach in random point with random velocity
    :return: list of cockroach's parameters appended to the main list
    '''
    x = randint(100, 800)
    y = randint(100, 800)
    size = 0.005 * randint(100, 100)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    cockroach(size, x, y, vx, vy)
    cockroaches.append([x, y, size, vx, vy])


def point_counter(k):
    '''
    the function determines whether you have hit the cockroach given its parameters
    :param k: list of the cockroach's parameters
    :return: True if you have hit it, otherwise False
    '''
    dist = ((k[0] - event.pos[0]) ** 2 + (k[1] - event.pos[1]) ** 2) ** 0.5
    if dist <= 500 * k[2]:
        return True
    else:
        return False


def cockroach_move(insects, time):
    '''
    the function calculates new positions of cockroaches with time and detects collisions
    :param insects: the list containing lists of all of the cockroaches' parameters
    :param time: remaining time until the end of the game
    :return: moving cockroaches on the screen
    '''
    draw_screen(time)
    for k in insects:
        k[0] += k[3]
        k[1] += k[4]
        cockroach(k[2], k[0], k[1], k[3], k[4])
        if k[0] < 250 * k[2] or k[0] > 900 - 250 * k[2]:
            k[3] *= - 1
        if k[1] < 500 * k[2] or k[1] > 900 - 500 * k[2]:
            k[4] *= -1


# drawing a cockroach image with pygame.draw
surface = draw_cockroach()
surface.set_colorkey(WHITE)

# initial cockroach spawning
for insect in range(0, 19):
    new_cockroach()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
closed = False

# processing events
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hit = False
            for guy in cockroaches:
                if point_counter(guy):
                    print('Hit!')
                    hit = True
                    cockroaches.remove(guy)
                    new_cockroach()
            if hit:
                i += 1
            else:
                print('Miss!')
    cockroach_move(cockroaches, timer)
    timer += -1
    if timer == 0:
        finished = True
    pygame.display.update()

# the end of a game
if closed:
    print("\nDon't be afraid! They could eat all your food!")
else:
    print("\nYou've killed", i, "cockroaches in 60 seconds. Good job!")

pygame.quit()
