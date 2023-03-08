from turtle import Turtle


class ScoreBoard(Turtle):
  def __init__(self, pos, screen_height):
    super().__init__()
    super().penup()
    cord = (-150, int(screen_height)/2-100)
    if pos == 'right':
      cord = (100, int(screen_height)/2-100)
    super().goto(cord)   
    super().hideturtle()
    super().color('#fff')
    self.score = 0
    self.display_score()

  def update_score(self):
    self.score += 1
    self.display_score()

  def display_score(self):
    super().clear()
    super().write(self.score, font=('Arial', 28, 'bold'))        