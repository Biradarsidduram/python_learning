from turtle import Turtle
from random import choice, randint

class Ball(Turtle):

  def __init__(self,screen):
    super().__init__(shape = 'circle')
    super().circle(radius=10)
    super().color('#fff')
    super().penup()
    self.screen = screen
    self.demarcation_line(screen)
    self.set_ball_direction()


  def set_ball_direction(self):
    super().home()
    directions = ['left', 'right']
    current_direction = choice(directions)
    self.direction = current_direction
    current_angle = randint(30, 80)
    if choice([0,1]) == 1:
      current_angle = -current_angle
    if current_direction == 'left':
      super().setheading(180 - current_angle)
    else:
      super().setheading(current_angle)

  def change_angle_on_top_bottom_window_hit(self):
    screen_height = int((self.screen.window_height())/2)-20
    current_angle = super().heading()
    current_y_pos = int(super().ycor())
    tilted_angle = 0
    if current_y_pos >= screen_height:
      if current_angle <= 90 and current_angle >= 0:
        tilted_angle = current_angle - 90
      elif current_angle > 90 and current_angle <= 180:
        tilted_angle = current_angle + 90
    if current_y_pos <= -screen_height:
      if current_angle >= 270 and current_angle <= 360:
        tilted_angle = current_angle + 90
      elif current_angle > 180 and current_angle < 270:
        tilted_angle = current_angle - 90

    if tilted_angle:
      tilted_angle = tilted_angle % 360
      super().setheading(tilted_angle)


  def change_angle_on_paddle_hit(self, paddle_pos):
    current_angle = super().heading()
    tilted_angle = 0
    random_angle =  randint(90, 120)
    if paddle_pos == 'left':
      if current_angle > 180 and current_angle < 270:
        tilted_angle = current_angle + random_angle
      elif current_angle < 180 and current_angle > 90:
        tilted_angle = current_angle - random_angle
    else:
      if current_angle < 360 and current_angle > 270:
        tilted_angle = current_angle - random_angle
      elif current_angle > 0 and current_angle < 90:
        tilted_angle = current_angle + random_angle

    if tilted_angle:
      tilted_angle = tilted_angle % 360
      super().setheading(tilted_angle)


  def move_forward(self):
    screen_width = int(int(self.screen.window_width())/2)-20
    current_x_pos = int(super().xcor())
    out_of_boundary = False
    player_pos = ''
    
    if current_x_pos < -screen_width:
      player_pos = 'right'
    elif current_x_pos > screen_width:
      player_pos = 'left'

    if current_x_pos < -screen_width or current_x_pos > screen_width:
      self.set_ball_direction()
      out_of_boundary = True
      return (out_of_boundary, player_pos)
    else:
      super().forward(10)
    self.change_angle_on_top_bottom_window_hit()
    return (out_of_boundary, 0)


  def demarcation_line(self, screen):
    demarcation_line = Turtle()
    demarcation_line.hideturtle()
    demarcation_line.pencolor('#fff')
    demarcation_line.setheading(90)
    demarcation_line.pensize(3)
    screen_height = int(screen.window_height())/2
    current_pos = int(demarcation_line.ycor())
    while current_pos <= screen_height:
      if demarcation_line.isdown():
        demarcation_line.penup()
      else:
        demarcation_line.pendown()
      demarcation_line.forward(20)
      current_pos = int(demarcation_line.ycor())

    demarcation_line.home()
    demarcation_line.setheading(270)
    current_pos = int(demarcation_line.ycor())
    while current_pos >= -screen_height:
      if demarcation_line.isdown():
        demarcation_line.penup()
      else:
        demarcation_line.pendown()
      demarcation_line.forward(20)
      current_pos = int(demarcation_line.ycor())