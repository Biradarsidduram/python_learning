# Tuple Graphics, Tuples and Importing Modules

from random import choice, randint
from turtle import Turtle as Purtle,Screen as Sn

screen = Sn()
screen.title("Welcome to the turtle Zoo")

colors = ['green yellow', 'medium blue', 'blue violet', 'indigo', 'orange red', 'maroon', 'gray', 'alice blue', 'medium spring green', 'red', 'black']

tim = Purtle()

tim.color('black')
tim.shape('arrow')
tim.resizemode('auto') 
screen.colormode(255)

tim.pos()

counter = 0

def shape(tim, length, sides):
  color = choice(colors)
  tim.pencolor(color)
  angle = (360/sides)
  for _ in range(sides):
    tim.forward(length)
    tim.right(angle)


def draw_shapes():
  for sides in range(3,11):
    shape(tim, 100, sides) 

# draw_shapes()


def random_walk(tim):
  directions = [0, 90, -90, 180]
  tim.width(15)
  tim.speed(10)
  tim.hideturtle()
  for _ in range(100):
    direction = choice(directions)
    # direction = randint(0, 360)
    tim.right(direction)
    color = get_random_rgb_value()
    tim.pencolor(color)
    for i in range(5):
      tim.forward(10)

def get_random_rgb_value():
  return (randint(0,255), randint(0,255), randint(0,255))

# random_walk(tim)

def circle(tim):
  tim.speed(10)
  tim.width(3)
  for i in range(0, 72):
    color = get_random_rgb_value()
    tim.color(color)
    tim.circle(100)
    tim.right(-5)

# circle(tim)

screen.exitonclick()