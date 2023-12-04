import pygame
import time
import random

pygame.init()

# ... (other code remains unchanged)

# loop
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
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # snake hits boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # update snake position
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

        # check if snake hits itself
        for x in snake[:-1]:
            if x == snake_head:
                game_close = True

        # draw the snake
        our_snake(snake_block, snake)

        # update the display
        pygame.display.update()

        # check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            snake_length += 1

        # set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# run the loop
gameloop()
