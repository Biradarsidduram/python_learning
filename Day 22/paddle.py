from turtle import Turtle
from time import sleep


class Paddle(Turtle):
  def __init__(self, screen, keys, pos='left'):
    super().__init__(shape = 'square')
    self.screen = screen
    if pos == 'right':
      screen_width = int(screen.window_width()/2)-20
    else:
      screen_width = -(int(screen.window_width()/2)-15)
    pos_cord = (screen_width,0)
    super().setheading(90)
    super().penup()
    super().shapesize(stretch_wid=1,stretch_len=4)
    super().resizemode('user')
    super().color('#fff')
    super().goto(pos_cord)
    screen.onkey(self.move_up, keys[0])
    screen.onkey(self.move_down, keys[1])

  def move_up(self):
    y_cor = int(super().ycor())
    screen_height = int(self.screen.window_height()/2)    
    if y_cor <= screen_height-60:
      super().forward(20)

  def move_down(self):
    y_cor = int(super().ycor())
    screen_height = int(self.screen.window_height()/2)    
    if y_cor >= -(screen_height -60):
      super().forward(-20)