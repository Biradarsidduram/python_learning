# Section 19 More Turtle Grpahics, Event listeners, State and Multiple Instances, High Order Functions

from turtle import Turtle, Screen
from random import randint
from os import system


system('clear')
screen = Screen()
screen.listen()




def tim_movement():
  tim = Turtle()
  tim.speed('fastest')

  def move_forward():
    tim.forward(10)

  def move_up():
    tim.setheading(90)
    move_forward()

  def move_down():
    tim.setheading(270)
    move_forward()

  def move_right():
    tim.setheading(0)
    move_forward()

  def move_left():
    tim.setheading(180)
    move_forward()


  def bind_keys(screen):
    screen.onkey(move_forward, 'space')
    screen.onkey(move_right, 'Right')
    screen.onkey(move_down, 'Down')
    screen.onkey(move_up, 'Up')
    screen.onkey(move_left, 'Left')
    screen.onkey(move_right, 'd')
    screen.onkey(move_up, 'w')
    screen.onkey(move_down, 's')
    screen.onkey(move_left, 'a')

  bind_keys(screen)


# Etch and Sktech App


def etch_and_sketch(screen):
  tim = Turtle()
  tim.speed('fastest')
  def move_forward():
    tim.forward(10)

  def move_backward():
    tim.forward(-10)

  def clock_angle(tim, clockWise = False):
    current_angle = tim.heading()
    if clockWise:
      current_angle -= 5
    else:
      current_angle += 5
    tim.setheading(current_angle)    

  def clock_wise():
    clock_angle(tim, True)

  def anti_clock_wise():
    clock_angle(tim)

  def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


  screen.onkeypress(clock_wise, 'Right')
  screen.onkeypress(move_forward, 'Up')
  screen.onkeypress(move_backward, 'Down')
  screen.onkeypress(anti_clock_wise, 'Left')
  screen.onkey(clear_screen, 'c')



screen.exitonclick()