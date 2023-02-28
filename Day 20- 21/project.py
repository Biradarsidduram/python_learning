# Snake Game

# Create a Snake body done
# Move the Snake done
# Control the Snake done
# Detect collison with food done
# Create a scoreboard done
# Detect collison with the Wall done
# Detect Collison with the Tail done

# New Feature
# Increase speeed by special button press
# Reverse Mode
# Want to play again


from turtle import Turtle, Screen
from time import sleep
from random import randint
from os import system

system('clear')

head_snake_direction = (0,0)
screen_width = 1000
screen_height = 1000
half_screen_width = screen_width/2 -20
half_screen_height = screen_height/2 -20
head_angle = 0
score = 0

def snake_game():
  screen = Screen()
  screen.tracer(0)
  screen.setup(width=screen_width, height=screen_height)
  screen.listen()
  screen.title("Snake Game \U0001F40D")
  screen.bgcolor('#000')
  screen_border = Turtle()
  screen_border.color('#fff')
  screen_border.hideturtle()
  screen_border.penup()
  screen_pos = [(-half_screen_width, -half_screen_height), (half_screen_width, -half_screen_height), (half_screen_width, half_screen_height), (-half_screen_width, half_screen_height), (-half_screen_width, -half_screen_height)]
  for pos in screen_pos:
    screen_border.goto(pos)
    screen_border.pendown()
  (snakes, food) = init_asset(screen) 
  

  bind_movement(screen, snakes, food)

  screen.exitonclick()

def render_score(screen):
  screen.title(f"Snake Game \U0001F40D, score : {score}")
  

def init_asset(screen):
  snakes = []
  render_score(screen)
  for count in range(3):
    snake = Turtle(shape = "square")
    snake.color('#fff')
    snake.penup()
    pos = (-20 *count, 0)
    snake.setpos(pos)
    snakes.append(snake)
  food = Turtle(shape = 'circle')
  food.color('green')
  food.penup()
  food_pos = get_food_pos()
  food.setpos(food_pos)
  food.width(snake.width())
  return (snakes, food)  

def get_food_pos():
  return (randint(- (half_screen_width -30), half_screen_height -30), randint(-(half_screen_width - 30),half_screen_height -30))

def bind_movement(screen, snakes, food):
  
  snake = snakes[0]

  def move_up():
    global head_snake_direction, head_angle
    current_angle = int(snake.heading())
    if current_angle != 270:
      head_snake_direction = snake.pos()
      head_angle = 90

  def move_down():
    global head_snake_direction, head_angle
    current_angle = int(snake.heading())
    if current_angle != 90:
      head_snake_direction = snake.pos()
      head_angle = 270
  
  def move_right():
    global head_snake_direction, head_angle
    current_angle = int(snake.heading())
    if current_angle != 180:
      head_snake_direction = snake.pos()
      head_angle = 0
  
  def move_left():
    global head_snake_direction, head_angle
    current_angle = int(snake.heading())
    if current_angle != 0:
      head_snake_direction = snake.pos()
      head_angle = 180

  def detect_wall_collision(snake):
    snake_pos_x = int(snake.xcor())
    snake_pos_y = int(snake.ycor())
    wall_pos = [-half_screen_width, half_screen_width,  half_screen_height, -half_screen_height]
    for pos in wall_pos:
      if pos in (snake_pos_x, snake_pos_y):
        return True
    return False
  
  def detect_food_collision(snake, food):
    snake_pos_x = int(snake.xcor())
    snake_pos_y = int(snake.ycor())
    food_pos_x = int(food.xcor())
    food_pos_y = int(food.ycor())
    difference_pos_x = 10000
    differnce_pos_y  = 10000
    if snake_pos_x > food_pos_x:
      difference_pos_x = snake_pos_x - food_pos_x
    else:
      difference_pos_x = food_pos_x - snake_pos_x
    if snake_pos_y > food_pos_y:
      differnce_pos_y = snake_pos_y - food_pos_y
    else:
      differnce_pos_y = food_pos_y - snake_pos_y
    if difference_pos_x <= 10 and differnce_pos_y <= 10:
      return True
    return False
  
  def detect_self_collision(snakes):
    head_snake_pos = snakes[0].pos()
    for snake in snakes[1:]:
      if snake.pos() == head_snake_pos:
        return True
    return False  

  def reset_food_pos(food):
    new_food_pos = get_food_pos()
    food.setpos(new_food_pos)

  def increase_snake_size(snakes):
    last_snake = snakes[-1]
    new_snake = Turtle(shape = "square")
    new_snake.color('#fff')
    new_snake.penup()
    last_snake_pos = last_snake.pos()
    if last_snake.heading() == 0:
     new_snake.setpos(last_snake_pos[0]-20, last_snake_pos[1])
    elif last_snake.heading() == 90:
      new_snake.setpos(last_snake_pos[0], last_snake_pos[1]+20)
    elif last_snake.heading() == 180:
      new_snake.setpos(last_snake_pos[0] + 20, last_snake_pos[1])
    elif last_snake_pos.heading() == 270:
      new_snake.setpos(last_snake_pos[0], last_snake_pos[1]-20)
    snakes.append(new_snake)

  def update_score(screen):
    global score
    score += 1
    render_score(screen)

  def render_game_over(snakes, food):
    game_over = Turtle()
    game_over.penup()
    game_over.color('red')
    game_over.setpos(-60, 0)
    game_over.hideturtle()
    food.hideturtle()
    for snake in snakes:
      snake.hideturtle()
    game_over.write("Game over ☠️", False, align='left', font=('Arial', 16, 'bold'))
    screen.update()
    
  def move_forward():
    global head_snake_direction, score, head_angle
    while True:
      if detect_food_collision(snake, food):
        reset_food_pos(food)
        increase_snake_size(snakes)
        update_score(screen)
      sleep(0.05)
      head_snake_direction = snake.pos()
      current_direction = head_snake_direction
      if snake.heading() != head_angle:
        snake.setheading(head_angle)
      snake.forward(10)
      previous_direction = 0

      for count in range(1,len(snakes)):
        previous_direction = snakes[count].pos()
        snakes[count].setpos(current_direction)
        current_direction = previous_direction

      if detect_wall_collision(snake) or detect_self_collision(snakes):
        render_game_over(snakes, food)
        return True
      
      screen.update()
      
      
  
  screen.onkeyrelease(move_forward, 'space')
  screen.onkeyrelease(move_right, 'Right')
  screen.onkeyrelease(move_down, 'Down')
  screen.onkeyrelease(move_up, 'Up')
  screen.onkeyrelease(move_left, 'Left')
  screen.onkeyrelease(move_right, 'd')
  screen.onkeyrelease(move_up, 'w')
  screen.onkeyrelease(move_down, 's')
  screen.onkeyrelease(move_left, 'a')

  move_forward()


def snake_movement(snake):
  snake.shapesize(None, 10, None)


snake_game()