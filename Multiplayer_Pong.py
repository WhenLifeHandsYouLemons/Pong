import pygame
import sys
import math
import random
from past.builtins.misc import execfile
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
pygame.display.set_caption("Multiplayer Pong")

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

middle_line_height = border_width
middle_line_width = border_height / 2
middle_line_x = (screen_width / 2) - (middle_line_width / 2)

ball_height = 20
ball_width = ball_height
ball_x = (screen_width / 2) - (ball_width / 2)
ball_y = (screen_height / 2) - (ball_height / 2)

multiplayer_current_score = [0, 0]

ball_speed = [10]

clock = pygame.time.Clock()

# For the design
def background_design_multiplayer_game():
    bg_colour = 0, 0, 0
    multiplayer_game.fill(bg_colour)
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (middle_line_x, 0, middle_line_width, middle_line_height))

def border_walls():
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (border_top_x, border_top_y, border_width, border_height))
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (border_bottom_x, border_bottom_y, border_width, border_height))

# For the player paddles
def multiplayer_paddles():
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_left_x, paddle_left_y, paddle_width, paddle_height))
    pygame.draw.rect(multiplayer_game, (255, 255, 255), (paddle_right_x, paddle_right_y, paddle_width, paddle_height))

# For the score display
def display_scores_multiplayer():
    score_left_x = middle_line_x - 130
    score_left_y = border_top_y + border_height + 5
    score_right_x = middle_line_x + middle_line_width + 5
    score_right_y = score_left_y
    score_left = multiplayer_current_score[0]
    score_right = multiplayer_current_score[1]
    # score_left = pygame.image.load(get_true_filename(f"{score_left}.jpg"))
    score_left = pygame.image.load(f"/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/score_images/{score_left}.jpg")
    multiplayer_game.blit(score_left, (score_left_x, score_left_y))
    # score_right = pygame.image.load(get_true_filename(f"{score_right}.jpg"))
    score_right = pygame.image.load(f"/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/score_images/{score_right}.jpg")
    multiplayer_game.blit(score_right, (score_right_x, score_right_y))

# For the ball movement
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
    
    def update(self, current_ball_speed):
        
        direction_radians = math.radians(self.direction)
    
        self.x += current_ball_speed * math.sin(direction_radians)
        self.y += current_ball_speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0 + border_height:
            self.direction = (180-self.direction)%360
    
        if self.y >= screen_height - (border_height * 2):
            self.direction = (180-self.direction)%360

        if self.x >= paddle_right_x:
            self.x = (screen_width / 2) - (ball_width / 2)
            self.y = (screen_height / 2) - (ball_height / 2)

            print("Left player gets a point")
            pygame.time.wait(2500)
            multiplayer_current_score.insert(0, multiplayer_current_score[0] + 1)
            print(multiplayer_current_score)
            multiplayer_current_score.remove(multiplayer_current_score[1])
            print(multiplayer_current_score)

        if self.x <= paddle_left_x:
            self.x = (screen_width / 2) - (ball_width / 2)
            self.y = (screen_height / 2) - (ball_height / 2)

            print("Right player gets a point")
            pygame.time.wait(2500)

            print(multiplayer_current_score)
            multiplayer_current_score.insert(1, multiplayer_current_score[1] + 1)
            print(multiplayer_current_score)
            multiplayer_current_score.pop(-1)
            print(multiplayer_current_score)

        if self.x <= paddle_left_x + paddle_width and self.y <= paddle_left_y + paddle_height and self.y >= paddle_left_y - ball_height:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

            current_ball_speed = current_ball_speed + 0.1
            ball_speed.append(current_ball_speed)
            ball_speed.pop(0)

        if self.x >= paddle_right_x - ball_width and self.y <= paddle_right_y + paddle_height and self.y >= paddle_right_y - ball_height:
            self.direction = (360-self.direction)%360 + random.randrange(0, 20)

            current_ball_speed = current_ball_speed + 0.1
            ball_speed.append(current_ball_speed)
            ball_speed.pop(0)

ball = Ball()
balls = pygame.sprite.Group()
balls.add(ball)

# Main loop
RUNNING_WINDOW = True
while RUNNING_WINDOW == True:

    clock.tick(29)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

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
    display_scores_multiplayer()
    
    balls.update(ball_speed[0])
    balls.draw(multiplayer_game)

    pygame.display.update()

    if multiplayer_current_score[0] == 11 or multiplayer_current_score[1] == 11:
        # execfile(get_true_filename("Game_Over_Screen.py"))
        execfile("C:/Users/2005s/Documents/Visual Studio Code/Python/Pygame/Pong/Game_Over_Screen.py")
        sys.exit()

sys.exit()