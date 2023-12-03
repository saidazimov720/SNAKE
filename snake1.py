import pygame
import time
import random

pygame.init()

#define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#set the screen width and height
dis_width = 800
dis_height = 600

#create the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Nurbek')
#set the font and size
font_style = pygame.font.SysFont(None, 50)
#set the snake block size and speed
snake_block = 10
snake_speed = 20
#initialize clock
clock = pygame.time.Clock()