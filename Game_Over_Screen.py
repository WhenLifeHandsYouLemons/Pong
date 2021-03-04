"""
Made By - Sooraj Sannabhadti
GitHub - https://github.com/WhenLifeHandsYouLemons
Twitter - https://twitter.com/LemonsHandYou
Instagram - https://www.instagram.com/whenlifehandsyoulemons1/
Latest Release - https://github.com/WhenLifeHandsYouLemons/Pong/releases
"""
import pygame
import sys
import os
pygame.init()

# For file searching when in .EXE format
def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)

screen_width = 960
screen_height = 600

multiplayer_game = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Over")

i = 5
while i != 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    # game_over_image = pygame.image.load(get_true_filename("game_over.jpg"))
    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")

    multiplayer_game.blit(game_over_image, (0, 0))

    pygame.time.wait(500)

    pygame.display.update()

    # game_over_image = pygame.image.load(get_true_filename("game_over_invert.jpg"))
    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over_invert.jpg")

    multiplayer_game.blit(game_over_image, (0, 0))

    pygame.time.wait(500)

    pygame.display.update()

    i = i - 1

# game_over_image = pygame.image.load(get_true_filename("game_over.jpg"))
game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")

multiplayer_game.blit(game_over_image, (0, 0))

pygame.display.update()

pygame.time.wait(2000)