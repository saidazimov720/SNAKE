# ... (previous code remains unchanged)

# Loop
def gameloop():
    global x1, y1, x1_change, y1_change, snake, snake_length, foodx, foody  # Declare variables as global

    game_over = False
    game_close = False

    while not game_over:
        for event in pygame
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

        # Snake hits boundaries
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
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake)

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Update the display
        pygame.display.update()

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the loop
gameloop()
