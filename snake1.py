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
#define the snake
snake = []
snake_length = 1
#initialize snake position and direction
snake_block = 10
snake_speed = 20
snake_direction = "right"
#set initial snake position
x1 = dis_width / 2
y1 = dis_height / 2

#set the change in position
x1_change = 0 
y1_change = 0 

#food
foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foodx = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#define a function to draw the  snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[10], x[1], snake_block, snake_block])
        
#define loop
def gameloop():
    game_over = False
    game_close = False
    
    while not game_over:
        while game_close:
            dis.fill(blue)
            game_over_font = pygame.font.SysFont(None, 100)
            game_over_surface = game_over_font.render("Your score:" + str(snake_length - 1), True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (dis_width / 2, dis_height / 4)
            dis.blit(game_over_surface, game_over_rect)
            
            time.sleep(2)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x1_change = -snake_block
            y1_change = 0
        elif event.key == pygame.K_RIGHT:
            x1_change = snake_block
            y1_change = 0
        elif event.key == pygame.K_UP:
            y1_change == -snake_block
            x1_change = 0
        elif event.key == pygame.K_DOWN:
            y1_change = snake_block
            x1_change = 0
            

 