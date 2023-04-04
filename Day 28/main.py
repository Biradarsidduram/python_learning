from tkinter import Tk, Label, Button, PhotoImage, Canvas
from time import sleep
from os import system


system('clear')


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_started = False
pomodoro_count = 0


root = Tk()
root.minsize(width=400, height=500)
root.title("Pomodoro Clock")
root.config(padx=100, pady = 50, bg=YELLOW)

def start_timer():
  global time_started, pomodoro_count
  break_mode = False
  mode_label.config(text="Work")
  if not time_started:
    time_started = True
    min_hand = WORK_MIN -1
    sec_hand = 60
    while time_started:
      if sec_hand == 0:
        min_hand -=1
        sec_hand = 59
      else:
        sec_hand -=1
      if min_hand == -1:
        if break_mode:
          min_hand = WORK_MIN -1
          break_mode = False
          mode_label.config(text="Work")
        else:  
          min_hand = SHORT_BREAK_MIN -1
          mode_label.config(text="Break", fg=RED)
          break_mode = True
          pomodoro_count +=1
        if pomodoro_count == 4:
          min_hand = LONG_BREAK_MIN -1
          break_mode = False
      new_timer_text = ''
      if min_hand < 10:
        new_timer_text = f"0{min_hand}:"
      else:
        new_timer_text = f"{min_hand}:"
      if sec_hand < 10:
        new_timer_text += f'0{sec_hand}'
      else:
        new_timer_text += f'{sec_hand}'
      tomatoe_img.itemconfig(timer_text, text=new_timer_text)
      sleep(1)
      root.update()
      


def reset_timer():
  global time_started, mode_label
  time_started = False
  tomatoe_img.itemconfig(timer_text, text='00:00')
  mode_label.config(text="Timer")


tomate_img_src = PhotoImage(file='tomato.png')
tomatoe_img = Canvas(width=200, height=222, bg=YELLOW, highlightthickness=0)
tomatoe_img.create_image(100,110, image = tomate_img_src)
timer_text = tomatoe_img.create_text(103,130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
mode_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg = GREEN,  bg=YELLOW)
pomodo_count_label = Label(text=f"Pomodoro session {pomodoro_count}", font=(FONT_NAME, 18, 'bold'), fg=RED, bg=YELLOW)

start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
start_button.config(bg='white')
reset_button.config(bg='white')
mode_label.pack()
tomatoe_img.pack()
start_button.pack(side='left')
reset_button.pack(side='right')

pomodo_count_label.pack(side="bottom")


root.mainloop()