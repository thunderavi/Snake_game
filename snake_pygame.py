import pygame
import time
import random
import pygame_gui
import pygame_menu
import pyganim

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set game clock
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10  # Decreased snake speed

# Define font style
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 45)

# Create a UI manager
ui_manager = pygame_gui.UIManager((width, height))

# Create a menu
menu = pygame_menu.Menu('Snake Game', width, height, theme=pygame_menu.themes.THEME_BLUE)

# Create a game over screen
def game_over_screen(score):
    dis.fill(blue)
    game_over_text = font_style.render("Game Over!", True, red)
    dis.blit(game_over_text, [width / 2 - 150, height / 2 - 50])
    score_text = score_font.render("Score: " + str(score), True, black)
    dis.blit(score_text, [width / 2 - 150, height / 2])
    play_again_text = font_style.render("Press C to play again", True, green)
    dis.blit(play_again_text, [width / 2 - 150, height / 2 + 50])
    quit_text = font_style.render("Press Q to quit", True, red)
    dis.blit(quit_text, [width / 2 - 150, height / 2 + 100])
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Create a title screen
def title_screen():
    dis.fill(blue)
    title = font_style.render("Snake Game", True, yellow)
    dis.blit(title, [width / 2 - 150, height / 2 - 50])
    instruction = font_style.render("Press Space to start", True, black)
    dis.blit(instruction, [width / 2 - 150, height / 2])
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Create a function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Create a function to display the score
def your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Create a function to display the level
def display_level(level):
    value = score_font.render("Level: " + str(level), True, black)
    dis.blit(value, [0, 30])

# Create a game loop
def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    level = 1

    while not game_over:

        while game_close == True:
            if game_over_screen(Length_of_snake - 1):
                game_close = False
                gameLoop()
            else:
                game_over = True

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

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)
        display_level(level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            if Length_of_snake % 5 == 0:
                level += 1
                snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Create a main function
def main():
    title_screen()
    gameLoop()

# Run the main function
if __name__ == "__main__":
    main()