# imports
import pygame
import random
import time


# initialise game
pygame.init()

# Color Globals

class GameColors():
    red = (255,0,0) # like a list, but cannot be changed
    orange = (255,127,0) # They are called Tuples
    yellow = (255,255,0)
    green = (0,255,0)
    blue = (0,0,255)
    violet = (127,0,255)
    brown = (102,51,0)
    black = (0,0,0)
    white = (255,255,255)

# adjust screen
class ScreenSize():
    width = 600
    height = 400

# Ball Globals
class Ball():
    ball_x = int(ScreenSize.width / 2)
    ball_y = int(ScreenSize.height / 2)
    ball_xv = 3
    ball_yv = 3
    ball_r = 20

# Paddle Globals
class Paddle():
    paddle1_x = 10
    paddle1_y = 10
    paddle1_w = 25
    paddle1_h = 100

    paddle2_x = ScreenSize.width - 35
    paddle2_y = 10
    paddle2_w = 25
    paddle2_h = 100

# Score Globals
class Score():
    player1 = 0
    player2 = 0

game_screen = pygame.display.set_mode((ScreenSize.width, ScreenSize.height))
pygame.display.set_caption("Tiny Tennis")
font = pygame.font.SysFont("monospace", 75)

pygame.mouse.set_visible(0) # makes mouse invisible whilst playing
do_main = True
while do_main:
    pressed = pygame.key.get_pressed()
    pygame.key.set_repeat
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            do_main = False

