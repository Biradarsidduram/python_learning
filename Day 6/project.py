# Robot Maze challenge

def turn_right():
  turn_left()
  turn_left()
  turn_left()
    
sound(True)
think(50)
 
while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif wall_in_front() and wall_on_right():
    turn_left()
  else:
    move()