import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size and caption
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
food_color = (0, 255, 0)

# Set the snake's initial position and size
snake_pos = [300, 300]
snake_body = [[300, 300], [290, 300], [280, 300]]
direction = "RIGHT"
change_to = direction

# Set the size of the food
food_size = 10

# Set the food position
food_pos = [random.randrange(1, (size[0] // food_size)) * food_size,
            random.randrange(1, (size[1] // food_size)) * food_size]
food_spawn = True

# Initialize the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Get the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update the direction if not conflicting
    direction = change_to

    # Move the snake in the direction
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # Add the current position to the snake's body
    snake_body.insert(0, list(snake_pos))

    # Check if the snake hit the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (size[0] // food_size)) * food_size,
                    random.randrange(1, (size[1] // food_size)) * food_size]
        food_spawn = True

    # Check if the snake hit the edge
    if snake_pos[0] >= size[0] or snake_pos[0] < 0 or snake_pos[1] >= size[1] or snake_pos[1] < 0:
        running = False

    # Check if the snake hit itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            running = False

    # Draw the snake and the food on the screen
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the screen and tick the clock
    pygame.display.update()
    clock.tick(15)

# Close the window and exit the program
pygame.quit()
