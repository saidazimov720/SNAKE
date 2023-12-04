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
dis_width = 600
dis_height = 400

# Create the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Nurbek')

# Set the font and size
font_style = pygame.font.SysFont(None, 30)

# Set the snake block size and speed
snake_block = 10
snake_speed = 15

# Initialize clock
clock = pygame.time.Clock()

# Define the snake
snake = [(dis_width / 2, dis_height / 2)]
snake_length = 1

# Initialize snake direction
snake_direction = "RIGHT"
change_to = snake_direction

# Set initial food position
foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, green, [x, y, snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Main game loop
game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Change the snake direction
    if change_to == "UP" and not snake_direction == "DOWN":
        snake_direction = "UP"
    elif change_to == "DOWN" and not snake_direction == "UP":
        snake_direction = "DOWN"
    elif change_to == "LEFT" and not snake_direction == "RIGHT":
        snake_direction = "LEFT"
    elif change_to == "RIGHT" and not snake_direction == "LEFT":
        snake_direction = "RIGHT"

    # Move the snake
    x, y = snake[0]
    if snake_direction == "UP":
        y -= snake_block
    elif snake_direction == "DOWN":
        y += snake_block
    elif snake_direction == "LEFT":
        x -= snake_block
    elif snake_direction == "RIGHT":
        x += snake_block

    # Check if snake eats the food
    if x == foodx and y == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Update the snake
    snake = [(x, y)] + snake[:snake_length - 1]

    # Check if snake hits the boundary
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        game_over = True

    # Check if snake hits itself
    for segment in snake[1:]:
        if segment == (x, y):
            game_over = True

    # Draw the background
    dis.fill(black)

    # Draw the food
    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

    # Draw the snake
    our_snake(snake_block, snake)

    # Display the score
    Your_score(snake_length - 1)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
quit()
