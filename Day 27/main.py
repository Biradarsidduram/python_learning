# Graphical User interfaces with Tkinter and Function Arguments

from tkinter import Tk, ttk, Label, Button, Entry, Radiobutton, Text, Checkbutton, Spinbox, Scale, Listbox, IntVar, StringVar
 
window = Tk()
window.title("My first GUI program")

window.minsize(width=500, height=300)


def button_click():
  label_value = input.get() or 'I am a label'
  label.config(text=label_value)
  spin_value = spinbox.get()
  print(spin_value)

def radio_click():
  print(radio_state.get())

def scale_select(value):
  print(scale_range.get())

def checkbox_select():
  print(checkbox_state.get())  

label = Label(text="I am a label", font=('Arial', 24, 'bold'))
button = Button(text="Subscribe Me", command=button_click)
input = Entry()
textarea = Text(undo=True, width=30, height=5)
radio_state = StringVar()
checkbox_state = StringVar()
radiobutton1 = Radiobutton(text="Option 1 ",  variable=radio_state, value="Hit me", command=radio_click)
radiobutton2 = Radiobutton(text="Option 2 ", variable=radio_state , value="Bite me", command=radio_click)
spinbox = Spinbox(values=[f'{num}' for num in range(10) ])
kill_me = Button(text="Kill me", command=window.destroy)
scale_range = Scale(command=scale_select)

checkbox_on = Checkbutton(text="Going to Trip?", onvalue="okay", offvalue="not_okay", variable=checkbox_state, command=checkbox_select)
checkbox_off = Checkbutton(text="Are you studying?", onvalue="okays", offvalue="not_okays", variable=checkbox_state, command=checkbox_select)
listbox = Listbox()

kill_me.pack() 
label.grid(row=0, column=0)
button.grid(row =0, column=2)
input.pack(row =0, column = 1)
spinbox.pack()
textarea.pack()
radiobutton1.pack()
radiobutton2.pack()
scale_range.pack()
checkbox_on.pack()
checkbox_off.pack()
listbox.pack()








# Function default arguments and keyword arguments -- Advanced Arguments

def my_function(a=1,b=2,c=3):
  return round(a + b + c, 3)

result = my_function(1,2,3)

print(type(result))

result = my_function(c=3,a=1.343,b=2)

print(type(result))

print(result)

# Unlimited arguments

def another_function(*args,**kwargs):
  sum = 0
  for value in args:
    sum += value
  for value in kwargs.values():
    sum += value
  return sum


result = another_function(1,2,3,4,5)

print(result)

result = another_function(2,3,a=1,b=3,c=4)

print(result)

class Car:

  def __init__(self, **kwargs):
    self.make =  kwargs.get('make') or "Ford" 
    self.model = kwargs.get('model') or '2007'

  def print_details(self):
    print(f"Car name is {self.make} and model number is {self.model}")

my_car  = Car(model = '2009')
my_car.print_details()

window.mainloop()