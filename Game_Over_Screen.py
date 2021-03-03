import pygame
pygame.init()

screen_width = 960
screen_height = 600

multiplayer_game = pygame.display.set_mode((screen_width, screen_height))

i = 5
while i != 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
    multiplayer_game.blit(game_over_image, (0, 0))

    pygame.time.wait(500)

    pygame.display.update()

    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over_invert.jpg")
    multiplayer_game.blit(game_over_image, (0, 0))

    pygame.time.wait(500)

    pygame.display.update()

    i = i - 1

game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
multiplayer_game.blit(game_over_image, (0, 0))

pygame.display.update()

pygame.time.wait(500)