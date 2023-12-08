import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the screen width and height
dis_width = 800
dis_height = 600

# Create the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by OpenAI')

# Set the font and size
font_style = pygame.font.SysFont(None, 50)

# Set the snake block size and speed
snake_block = 10
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Define the snake
snake = []
snake_length = 1

# Initialize snake position and direction
snake_block = 10
snake_speed = 15
snake_direction = "RIGHT"

# Set initial snake position
x1 = dis_width / 2
y1 = dis_height / 2

# Set the change in position
x1_change = 0
y1_change = 0

# Set initial food position
foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# Define a function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Define the game loop
def gameLoop():
    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            dis.fill(blue)
            game_over_font = pygame.font.SysFont(None, 100)
            game_over_surface = game_over_font.render("Your Score : " + str(snake_length - 1), True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (dis_width / 2, dis_height / 4)
            dis.blit(game_over_surface, game_over_rect)
            pygame.display.flip()

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
                        gameLoop()

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
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake hits the boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        # Check if snake hits itself
        for x in snake[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake)

        # Update the display
        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game loop
gameLoop()
