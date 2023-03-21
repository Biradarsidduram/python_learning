from turtle import Turtle, Screen
from pandas import read_csv, DataFrame
from time import sleep

from os import system


system('clear')


screen_width = 1000
screen_height = 800

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)


data = read_csv('50_states.csv')

states = data['state'].to_list()
missed_states = states[::]
user_entered_states = []

condition = True

while condition:
  state_name = screen.textinput(prompt="What's another state name?", title=f'{len(user_entered_states)}/{len(states)} States Correct')

  if state_name and state_name in states:
    sleep(0.5)
    user_entered_states.append(state_name)
    state_turtle = Turtle()
    state_turtle.penup()
    pos = (data[data['state'] == state_name][['x', 'y']])
    cord = (int(pos['x']), int(pos['y']))
    state_turtle.goto(cord)
    state_turtle.write(state_name)
    state_turtle.hideturtle()
    missed_states.remove(state_name)
    screen.update()

  if (len(user_entered_states) == len(states)) or state_name == 'Exit':
    condition = False

if len(missed_states):
  DataFrame({
    'missed_states': missed_states
  }).to_csv('missed_states.csv')

screen.exitonclick()