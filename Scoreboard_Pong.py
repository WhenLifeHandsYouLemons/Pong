import sys
import pygame
pygame.init()

clock = pygame.time.Clock()

screen_width = 960
screen_height = 600

multiplayer_game = pygame.display.set_mode((screen_width, screen_height))
leaderboard_screen = pygame.display.set_mode((screen_width, screen_height))
title_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Scoreboard")

ball_height = 20
ball_width = ball_height

select_x = (screen_width / 2) - (ball_width / 2)
select_y = (screen_height / 2) - (ball_height / 2) - 100

game_select_x = (screen_width / 2) - (ball_width / 2)
game_select_y = (screen_height / 2) - (ball_height / 2)
game_select_width = ball_width
game_select_height = game_select_width
game_select_speed = 10

exit_button_width = 300
exit_button_height = 75
exit_button_x = (screen_width / 2) - (exit_button_width / 2)
exit_button_y = 450
leaderboard_exit_button_y = exit_button_y + 50

border_height = 12

def background_design_leaderboard_screen():
    bg_colour = (0, 0, 0)
    leaderboard_screen.fill(bg_colour)

    pygame.draw.rect(leaderboard_screen, (255, 255, 255), (select_x, select_y, game_select_width, game_select_height))
    pygame.draw.rect(title_screen, (255, 255, 255), (exit_button_x - 5, leaderboard_exit_button_y - 5, exit_button_width + 10, exit_button_height + 10))
    
    exit_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/exit_game.jpg")
    leaderboard_screen.blit(exit_image, (exit_button_x, leaderboard_exit_button_y))


RUNNING_WINDOW = True
while RUNNING_WINDOW == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    clock.tick(29)

    multiplayer_game.blit(leaderboard_screen, (0, 0))

    background_design_leaderboard_screen()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and select_y > border_height:
        select_y -= game_select_speed
        print("Select moved up")
    if keys[pygame.K_DOWN] and select_y < screen_height - game_select_width:
        select_y += game_select_speed
        print("Select moved down")
    if keys[pygame.K_LEFT] and select_x > border_height:
        select_x -= game_select_speed
        print("Select moved left")
    if keys[pygame.K_RIGHT] and select_x < screen_width - game_select_width:
        select_x += game_select_speed
        print("Select moved right")

    while select_x >= exit_button_x and select_x <= exit_button_x + exit_button_width - game_select_width and select_y >= leaderboard_exit_button_y and select_y <= leaderboard_exit_button_y + exit_button_height - game_select_height and RUNNING_WINDOW:
        sys.exit()

    pygame.display.update()
