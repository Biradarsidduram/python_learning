# Pong Game Steps

'''
1. Create the Screen done
2. Create and move a paddle done
3. Create another paddle done
4. Create the ball and make it move done
5. Detect Collision with wall and bounce done
6. Detect Collision with paddle done
7. Detect when paddle misses done
8. Keep Score done
'''

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from time import sleep
from os import system

system('clear')

screen_width = 1400
screen_height = 900



screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('#000')
screen.tracer(2)
screen.listen()

paddle1 = Paddle(screen = screen, keys=['w', 's'])
paddle2 = Paddle(screen = screen, keys = ['Up', 'Down'],  pos='right')

paddle1_score = ScoreBoard(pos='left', screen_height=screen_height)
paddle2_score = ScoreBoard(pos='right', screen_height=screen_height)

ball = Ball(screen)


while True:
  sleep(0.03)
  (out_of_boundary, player_pos) = ball.move_forward()
  ball_x_cor = int(ball.xcor())
  ball_y_cor = int(ball.ycor())
  paddle1_x_cor = int(paddle1.xcor())
  paddle1_y_cor = int(paddle1.ycor())
  paddle2_x_cor = int(paddle2.xcor())
  paddle2_y_cor = int(paddle2.ycor())

  if out_of_boundary:
    if player_pos == 'right':
      paddle2_score.update_score()
    else:
      paddle1_score.update_score()
 
  if abs(paddle1_x_cor - ball_x_cor) < 20 and abs(paddle1_y_cor - ball_y_cor) < 40:
    ball.change_angle_on_paddle_hit('left')
  if abs(paddle2_x_cor - ball_x_cor) < 20 and abs(paddle2_y_cor - ball_y_cor) < 40:
    ball.change_angle_on_paddle_hit('right')

  screen.update()
