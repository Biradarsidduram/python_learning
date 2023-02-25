from turtle import Turtle, Screen
from random import randint, random
from os import system

system('clear')

screen_width = 800
screen_height = 800

screen = Screen()


def turtle_racing(screen):
  print("Turtle Racing Game")
  screen.title("Turtle Racing Game")
  screen.setup(width = screen_width, height = screen_height)
  user_color = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race ? Enter a color : ")
  turtles = setup_turtles()
  start_race(turtles, user_color)  

def setup_turtles():
  turtles = []
  colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
  for index in range(len(colors)):
    new_turtle = Turtle()
    color = colors[index]
    new_turtle.color(color)
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.speed = randint(1,7)
    pos = (-(screen_width/2 -10), -100 + 30 * index)
    new_turtle.goto(pos)
    turtles.append(new_turtle)
  return turtles   

def start_race(turtles, user_color):
  while True:
    for turtle in turtles:
      turtle.forward(turtle.speed)
      current_pos_x = int(turtle.pos()[0])
      current_turtle_color = turtle.color()[0]
      if current_pos_x >= screen_width / 2 - 10:
        if current_turtle_color == user_color:
          print(f"Your turtle {user_color} has won the race.")
        else:
          print(f"You lost the game by Turtle {current_turtle_color}")
        return


turtle_racing(screen)

screen.exitonclick()