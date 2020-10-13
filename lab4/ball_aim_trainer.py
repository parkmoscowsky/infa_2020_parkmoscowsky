# pygame events

import pygame
from pygame.draw import *
from random import randint
pygame.init()

# setting FPS && screen size
FPS = 2
screen = pygame.display.set_mode((1200, 900))

# coloring
DARK_SALMON = (233, 150, 122)
ORCHID = (218, 112, 214)
KHAKI = (240, 230, 140)
BLACK = (0, 0, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [BLACK, DARK_SALMON, ORCHID, KHAKI, MAGENTA, CYAN, WHITE]

# declaring global variables
global x, y, r

# setting counters' starting values
i = 0
j = 0
k = 1


# defining way too many functions
def new_ball():
    '''
    function creates a new ball on the screen
    :return: ball drawn on a pygame surface
    '''
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click():
    '''
    function prints parameters of created ball
    :return: position and radius of created ball
    '''
    global x, y, r
    print(x, y, r)


def point_counter():
    '''
    function returns your points based on whether you've hit the ball or not
    :return: 1 if hit, 0 if miss
    '''
    global x, y, r
    dist = ((x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) ** 0.5
    if dist <= r:
        return 1
    else:
        return 0


# processing pygame events
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            i += k * point_counter()
            k = 0
            j += 1
    k = 1
    new_ball()
    click()
    pygame.display.update()
    screen.fill(WHITE)

# in the end of the game
if j != 0:
    print('\nyour aim is', round(100 * i / j), '%\ngood job!')
else:
    print("\ndon't be so shy, try again!")
pygame.quit()
