from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.color('#000')
        self.hideturtle()
        self.screen_width = screen_width
        self.screen_height = screen_height 
        self.score = 1
        self.write_score()

    def update_level(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        pen_pos = (-(self.screen_width/2-10), self.screen_height/2-50)
        self.clear()
        self.setpos(pen_pos)
        self.write(f"Level {self.score}", font=FONT)

    def game_over(self):
        self.clear()
        pen_pos = (-40, 0)
        self.setpos(pen_pos)
        self.write("Game Over \U0001F3B2", font=FONT)    