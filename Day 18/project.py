# The Hirst painting Project
from turtle import Turtle, Screen
from random import choice
import colorgram


def get_extracted_colors():
  colors = colorgram.extract('./hirst dot painting.jpg', 30)
  rgb_colors= []
  for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
  return rgb_colors

def hirst_dot_painting():
  paint = Turtle()
  paint.shape('arrow')
  paint.speed('fastest')
  screen = Screen()
  screen.colormode(255)
  rgb_colors = get_extracted_colors()
  paint.penup()
  for i in range(10):
    y_pos = -200 + (50 * i)
    paint.setposition(0, y_pos)
    for i in range(10):
      color = choice(rgb_colors)
      paint.pendown()
      paint.begin_fill()
      paint.circle(10)
      paint.pencolor('#fff')
      paint.fillcolor(color)
      paint.end_fill()
      paint.penup()
      paint.forward(50)
      paint.fillcolor('#000')

  screen.exitonclick()

hirst_dot_painting()  