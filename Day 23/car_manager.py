from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, screen_width, screen_height):
        self.cars_list = []
        self.screen_width = screen_width
        self.screen_height = screen_height

    def add_car(self):
        car = Car(self.screen_width, self.screen_height)
        self.cars_list.append(car)

    def delete_car_by_index(self, index):
        del self.cars_list[index]

class Car(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape('square')
        random_color = choice(COLORS)
        self.penup()
        self.setheading(180)
        self.color(random_color)
        self.resizemode('auto')
        self.shapesize(stretch_wid=1, stretch_len=2)
        car_pos = ((screen_width)/2-20, randint(-(screen_height/2-50), screen_height/2-50))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.setpos(car_pos)

    def move_forward(self, level):
        speed = 10 + 5 * level
        self.forward(speed)

    def is_reached_end(self):
        car_pos = int(self.xcor())
        x_pos = -(self.screen_width/2+20)
        return car_pos <= x_pos
