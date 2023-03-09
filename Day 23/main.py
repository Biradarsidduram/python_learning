from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from os import system

# Create a turtle plyaer that start at the bottom of the screen and listen for the up keypress to move the turtle north done
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (Safe zone). Hint gemerate a mew car only every 6th time the game loop runs. done
# Detect when the turtle player collides with the a car and stop the game if this happens.  done
# Detect when the turtle player has reached the top edge of the screen (Finish Line). When this happens, return the turtle to the starting position and increase the cars speed. Hint think about creating an attribute and using the MOVE_Increment to increase the car speed. done
# Create a scoreboard that keep tracks of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. done

system('clear')

screen_width = 800
screen_height = 800

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

screen.listen()

game_is_on = True

turtle = Player(screem_width=screen_width, screen_height=screen_height)
score_board = Scoreboard(screen_width=screen_width, screen_height=screen_height)

count = 0
level = 0

car_manager = CarManager(screen_height=screen_height, screen_width=screen_width)

screen.onkey(turtle.move_up, 'Up')

while game_is_on:
    sleep(0.1)
    screen.update()
    count +=1

    if count % 6 == 0:
        car_manager.add_car()

    for index, car in enumerate(car_manager.cars_list):
        car.move_forward(level)
        if car.is_reached_end():
            car.hideturtle()
            if index:
                car_manager.delete_car_by_index(index)
        if car.distance(turtle) < 20:
            game_is_on = False
            score_board.game_over()

    turtle_y_pos = int(turtle.ycor())

    if turtle_y_pos >= screen_height/2-20:
        turtle.reset_pos()
        score_board.update_level()
        level += 1



screen.exitonclick()