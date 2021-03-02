import pygame
import random
import math
import sys
import time
pygame.init()

screen_width = 960
screen_height = 600

multiplayer_game = pygame.display.set_mode((screen_width, screen_height))
title_screen = pygame.display.set_mode((screen_width, screen_height))
leaderboard_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

border_width = 960
border_height = 12
border_top_x = 0
border_top_y = 0
border_bottom_x = 0
border_bottom_y = 600 - border_height

paddle_height = 120
paddle_width = 20
paddle_left_x = 10
paddle_left_y = 300 - (paddle_height / 2)
paddle_right_x = 960 - paddle_width - 10
paddle_right_y = 300 - (paddle_height / 2)
paddle_speed = 9

left_border_height = 600
left_border_width = 10 + paddle_width

ball_height = 20
ball_width = ball_height
ball_x = (screen_width / 2) - (ball_width / 2)
ball_y = (screen_height / 2) - (ball_height / 2)

middle_line_height = border_width
middle_line_width = border_height / 2
middle_line_x = (screen_width / 2) - (middle_line_width / 2)

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
leaderboard_exit_button_y = exit_button_y + 50

select_x = (screen_width / 2) - (ball_width / 2)
select_y = (screen_height / 2) - (ball_height / 2) - 100

i = 7

multiplayer_current_score = [0, 0]

singleplayer_current_score = [0, 0]

oneplayer_lost = 0

clock = pygame.time.Clock()


def background_design_multiplayer_game():
#https://www.youtube.com/watch?v=i1rEdG6Oeno - For how to change the background colour
    bg_colour = 0, 0, 0
    multiplayer_game.fill(bg_colour)
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (middle_line_x, 0, middle_line_width, middle_line_height))


def border_walls():
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (border_top_x, border_top_y, border_width, border_height))
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (border_bottom_x, border_bottom_y, border_width, border_height))


def multiplayer_paddles():
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_left_x, paddle_left_y, paddle_width, paddle_height))
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_right_x, paddle_right_y, paddle_width, paddle_height))


def singleplayer_paddles():
    paddle_left_x = 0
    paddle_left_y = 0

    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_left_x, paddle_left_y, left_border_width, left_border_height))
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_right_x, paddle_right_y, paddle_width, paddle_height))


def display_scores():
    score_left_x = middle_line_x - 130
    score_left_y = border_top_y + border_height + 5
    score_right_x = middle_line_x + middle_line_width + 5
    score_right_y = score_left_y
    score_left = multiplayer_current_score[0]
    score_right = multiplayer_current_score[1]
#CHANGE THE DIRECTORY BEFORE SENDING IT IN
    score_left = pygame.image.load(f"/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/score_images/{score_left}.jpg")
    multiplayer_game.blit(score_left, (score_left_x, score_left_y))
#CHANGE THE DIRECTORY BEFORE SENDING IT IN
    score_right = pygame.image.load(f"/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/score_images/{score_right}.jpg")
    multiplayer_game.blit(score_right, (score_right_x, score_right_y))


def background_design_title_screen():
    background_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/no score background.jpg")
    
    title_screen.blit(background_image, (0, 0))
    
    pygame.draw.rect(title_screen, (255, 255, 255), (game_select_x, game_select_y, game_select_width, game_select_height))
    pygame.draw.rect(title_screen, (255, 255, 255), (exit_button_x - 5, exit_button_y - 5, exit_button_width + 10, exit_button_height + 10))
    pygame.draw.rect(title_screen, (255, 255, 255), (singleplayer_button_x - 5, singleplayer_button_y - 5, singleplayer_button_width + 10, singleplayer_button_height + 10))
    pygame.draw.rect(title_screen, (255, 255, 255), (multiplayer_button_x - 5, multiplayer_button_y - 5, multiplayer_button_width + 10, multiplayer_button_height + 10))
    
    multiplayer_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/two_player.jpg")
    title_screen.blit(multiplayer_image, (multiplayer_button_x, multiplayer_button_y))
    
    singleplayer_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/one_player.jpg")
    title_screen.blit(singleplayer_image, (singleplayer_button_x, singleplayer_button_y))
    
    exit_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/exit_game.jpg")
    title_screen.blit(exit_image, (exit_button_x, exit_button_y))


def background_design_leaderboard_screen():
    bg_colour = (0, 0, 0)
    leaderboard_screen.fill(bg_colour)

    pygame.draw.rect(leaderboard_screen, (255, 255, 255), (select_x, select_y, game_select_width, game_select_height))
    pygame.draw.rect(title_screen, (255, 255, 255), (exit_button_x - 5, leaderboard_exit_button_y - 5, exit_button_width + 10, exit_button_height + 10))
    
    exit_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/title_screen_images/exit_game.jpg")
    leaderboard_screen.blit(exit_image, (exit_button_x, leaderboard_exit_button_y))


def background_design_singleplayer_game():
    bg_colour = 0, 0, 0
    multiplayer_game.fill(bg_colour)


# I used the code for the ball from another program but I couldn't find it again.
class Ball(pygame.sprite.Sprite):
    image = pygame.Surface([ball_width, ball_height])
    direction = random.randrange(45, 135)
    x = ball_x
    y = ball_y

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ball_colour = (255, 255, 255)
    
        self.image.fill(ball_colour)
        self.rect = self.image.get_rect()
    
    def update(self):
        ball_speed = 10
        direction_radians = math.radians(self.direction)
    
        self.x += ball_speed * math.sin(direction_radians)
        self.y += ball_speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0 + border_height:
            self.direction = (180-self.direction)%360
    
        if self.y >= screen_height - (border_height * 2):
            self.direction = (180-self.direction)%360

        if self.x >= paddle_right_x and paddle_left_x != 0:
            self.x = (screen_width / 2) - (ball_width / 2)
            self.y = (screen_height / 2) - (ball_height / 2)
    
            print("Lost")
            time.sleep(2.5)

#http://zetcode.com/lang/python/lists/ - For how to insert an integer to a list
            multiplayer_current_score.insert(0, multiplayer_current_score[0] + 1)
            print(multiplayer_current_score)
            multiplayer_current_score.remove(multiplayer_current_score[1])
            print(multiplayer_current_score)

        if self.x >= paddle_right_x and paddle_left_x == 0:
            self.x = (screen_width / 2) - (ball_width / 2)
            self.y = (screen_height / 2) - (ball_height / 2)
    
            print("Lost")
            time.sleep(2.5)

        if self.x <= paddle_left_x and paddle_left_y != 0:
            self.x = (screen_width / 2) - (ball_width / 2)
            self.y = (screen_height / 2) - (ball_height / 2)

            print("Lost")
            time.sleep(2.5)

            print(multiplayer_current_score)
            multiplayer_current_score.insert(1, multiplayer_current_score[1] + 1)
            print(multiplayer_current_score)
#https://stackoverflow.com/questions/18169965/how-to-delete-last-item-in-list - For how to remove the last item in a list
            del multiplayer_current_score[-1]
            print(multiplayer_current_score)

        if self.x <= paddle_left_x + left_border_width and paddle_left_y == 0:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

#https://stackoverflow.com/questions/22901056/how-do-i-make-the-ball-bounce-off-the-paddle - For how to make the ball bounce off the paddle
        if self.x <= paddle_left_x + paddle_width and self.y <= paddle_left_y + paddle_height and self.y >= paddle_left_y - ball_height and paddle_left_x != 0:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

        if self.x <= 0 + paddle_width and game_select_x >= singleplayer_button_x and game_select_x <= singleplayer_button_x + singleplayer_button_width - game_select_width and game_select_y >= singleplayer_button_y and game_select_y <= singleplayer_button_y + singleplayer_button_height - game_select_height:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

        if self.x >= paddle_right_x - ball_width and self.y <= paddle_right_y + paddle_height and self.y >= paddle_right_y - ball_height:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

            if paddle_left_x == 0:
                if singleplayer_current_score[1] == 9:
                    singleplayer_current_score.append(0, singleplayer_current_score[1] + 1)
                    del singleplayer_current_score[-1]
                    print(singleplayer_current_score)

        if self.x >= paddle_right_x and paddle_left_x == 0:
            oneplayer_lost = True
        elif self.x <= paddle_right_x and paddle_left_x == 0:
            oneplayer_lost = False

ball = Ball()
balls = pygame.sprite.Group()
balls.add(ball)



RUNNING_WINDOW = True

############################################################ Main loop
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

##############################################################      EXIT GAME
    while game_select_x >= exit_button_x and game_select_x <= exit_button_x + exit_button_width - game_select_width and game_select_y >= exit_button_y and game_select_y <= exit_button_y + exit_button_height - game_select_height and RUNNING_WINDOW:
        sys.exit()

##############################################################      MULTIPLAYER
    while game_select_x >= multiplayer_button_x and game_select_x <= multiplayer_button_x + multiplayer_button_width - game_select_width and game_select_y >= multiplayer_button_y and game_select_y <= multiplayer_button_y + multiplayer_button_height - game_select_height and RUNNING_WINDOW:

        clock.tick(29)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False

        multiplayer_game.blit(title_screen, (0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and paddle_right_y > border_height:
            paddle_right_y -= paddle_speed
            print("Right paddle moved up")
        if keys[pygame.K_DOWN] and paddle_right_y < screen_height - paddle_height - border_height:
            paddle_right_y += paddle_speed
            print("Right paddle moved down")

        if keys[pygame.K_w] and paddle_left_y > border_height:
            paddle_left_y -= paddle_speed
            print("Left paddle moved up")
        if keys[pygame.K_s] and paddle_left_y < screen_height - paddle_height - border_height:
            paddle_left_y += paddle_speed
            print("Left paddle moved down")

        background_design_multiplayer_game()
        border_walls()
        multiplayer_paddles()
        display_scores()
        
        balls.update()
        balls.draw(multiplayer_game)

        pygame.display.update()

        if multiplayer_current_score[0] == 11 or multiplayer_current_score[1] == 11:
            while i > 0:
                game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
                multiplayer_game.blit(game_over_image, (0, 0))

                time.sleep(0.5)

                pygame.display.update()

                game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over_invert.jpg")
                multiplayer_game.blit(game_over_image, (0, 0))

                time.sleep(0.5)
                i = i - 1

                pygame.display.update()

            game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
            multiplayer_game.blit(game_over_image, (0, 0))

            pygame.display.update()

            time.sleep(2)
            sys.exit()

##################################################################      SINGLE PLAYER
    while game_select_x >= singleplayer_button_x and game_select_x <= singleplayer_button_x + singleplayer_button_width - game_select_width and game_select_y >= singleplayer_button_y and game_select_y <= singleplayer_button_y + singleplayer_button_height - game_select_height and RUNNING_WINDOW:

        clock.tick(29)
        paddle_left_x = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False

        multiplayer_game.blit(title_screen, (0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and paddle_right_y > border_height:
            paddle_right_y -= paddle_speed
            print("Right paddle moved up")
        if keys[pygame.K_DOWN] and paddle_right_y < screen_height - paddle_height - border_height:
            paddle_right_y += paddle_speed
            print("Right paddle moved down")

        background_design_singleplayer_game()
        border_walls()
        singleplayer_paddles()
        display_scores()
        
        balls.update()
        balls.draw(multiplayer_game)

        if oneplayer_lost == True:
            print("Lost in singleplayer")

            while RUNNING_WINDOW:
                print("Showing scoreboard")
                while i > 0:
                    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
                    multiplayer_game.blit(game_over_image, (0, 0))
                    time.sleep(0.5)

                    pygame.display.update()

                    game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over_invert.jpg")
                    multiplayer_game.blit(game_over_image, (0, 0))

                    time.sleep(0.5)
                    i = i - 1

                    pygame.display.update()

                game_over_image = pygame.image.load("/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/game_over_images/game_over.jpg")
                multiplayer_game.blit(game_over_image, (0, 0))

                pygame.display.update()

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
            
        pygame.display.update()

    pygame.display.update()





pygame.quit()
