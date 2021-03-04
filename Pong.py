import pygame
import sys
import os
from past.builtins.misc import execfile
pygame.init()

# For file searching when in .EXE format
def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)

# Variables
screen_width = 960
screen_height = 600

title_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Testing Pong")

border_width = 960
border_height = 12

ball_height = 20
ball_width = ball_height
ball_x = (screen_width / 2) - (ball_width / 2)
ball_y = (screen_height / 2) - (ball_height / 2)

game_select_x = (screen_width / 2) - (ball_width / 2)
game_select_y = (screen_height / 2) - (ball_height / 2)
game_select_width = ball_width
game_select_height = game_select_width
game_select_speed = 10

multiplayer_button_width = 275
multiplayer_button_height = 75
multiplayer_button_x = ball_x + ball_width + 100
multiplayer_button_y = (screen_height / 2) - (multiplayer_button_height / 2) + 50

singleplayer_button_width = 275
singleplayer_button_height = 75
singleplayer_button_x = ball_x - singleplayer_button_width - 100
singleplayer_button_y = (screen_height / 2) - (singleplayer_button_height / 2) + 50

exit_button_width = 300
exit_button_height = 75
exit_button_x = (screen_width / 2) - (exit_button_width / 2)
exit_button_y = 450

clock = pygame.time.Clock()

# For the design
def background_design_title_screen():
    # background_image = pygame.image.load(get_true_filename("no score background.jpg"))
    background_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/no score background.jpg")
    title_screen.blit(background_image, (0, 0))

    pygame.draw.rect(title_screen, (255, 255, 255), (game_select_x, game_select_y, game_select_width, game_select_height))
    pygame.draw.rect(title_screen, (255, 255, 255), (exit_button_x - 5, exit_button_y - 5, exit_button_width + 10, exit_button_height + 10))
    pygame.draw.rect(title_screen, (255, 255, 255), (singleplayer_button_x - 5, singleplayer_button_y - 5, singleplayer_button_width + 10, singleplayer_button_height + 10))
    pygame.draw.rect(title_screen, (255, 255, 255), (multiplayer_button_x - 5, multiplayer_button_y - 5, multiplayer_button_width + 10, multiplayer_button_height + 10))

    # multiplayer_image = pygame.image.load(get_true_filename("two_player.jpg"))
    multiplayer_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/two_player.jpg")
    title_screen.blit(multiplayer_image, (multiplayer_button_x, multiplayer_button_y))

    # singleplayer_image = pygame.image.load(get_true_filename("one_player.jpg"))
    singleplayer_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/one_player.jpg")
    title_screen.blit(singleplayer_image, (singleplayer_button_x, singleplayer_button_y))

    # exit_image = pygame.image.load(get_true_filename("exit_game.jpg"))
    exit_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/exit_game.jpg")
    title_screen.blit(exit_image, (exit_button_x, exit_button_y))

# Main loop
RUNNING_WINDOW = True
while RUNNING_WINDOW:
    clock.tick(29)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and game_select_y > border_height:
        game_select_y -= game_select_speed
        print("Game select moved up")
    if keys[pygame.K_DOWN] and game_select_y < screen_height - game_select_width:
        game_select_y += game_select_speed
        print("Game select moved down")
    if keys[pygame.K_LEFT] and game_select_x > border_height:
        game_select_x -= game_select_speed
        print("Game select moved left")
    if keys[pygame.K_RIGHT] and game_select_x < screen_width - game_select_width:
        game_select_x += game_select_speed
        print("Game select moved right")

    background_design_title_screen()

    # Exit game
    while game_select_x >= exit_button_x and game_select_x <= exit_button_x + exit_button_width - game_select_width and game_select_y >= exit_button_y and game_select_y <= exit_button_y + exit_button_height - game_select_height and RUNNING_WINDOW:
        sys.exit()

    # Multiplayer
    while game_select_x >= multiplayer_button_x and game_select_x <= multiplayer_button_x + multiplayer_button_width - game_select_width and game_select_y >= multiplayer_button_y and game_select_y <= multiplayer_button_y + multiplayer_button_height - game_select_height and RUNNING_WINDOW:
        # execfile(get_true_filename("Multiplayer_Pong.py"))
        execfile("C:/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/Multiplayer_Pong.py")

    # Singleplayer
    while game_select_x >= singleplayer_button_x and game_select_x <= singleplayer_button_x + singleplayer_button_width - game_select_width and game_select_y >= singleplayer_button_y and game_select_y <= singleplayer_button_y + singleplayer_button_height - game_select_height and RUNNING_WINDOW:
        # execfile(get_true_filename("Singleplayer_Pong.py"))
        execfile("C:/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/Singleplayer_Pong.py")

    pygame.display.update()

sys.quit()
