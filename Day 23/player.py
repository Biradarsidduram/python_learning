from turtle import Turtle

class Player(Turtle):

    def __init__(self,screem_width, screen_height):
        super().__init__(shape='turtle')
        self.color('#000')
        self.penup()
        pos = (0, - (screen_height/2 - 20))
        self.setpos(pos)
        self.setheading(90)
        self.screen_width = screem_width
        self.screen_height = screen_height

    def move_up(self):
        self.forward(10)
        
    def reset_pos(self):
        y_cor = -(self.screen_height/2-20)
        pos = (0, y_cor)
        self.setpos(pos)