# Building a Password Manager GUI App

# Create a GUI for storing password
# Widgets includes Website name, Email/UserName, Password all are inputs and generate password button which generates random password and add it to the password input
# Create a wodget Add button, upon click which should open an alert message which must shows to the user email and password
# After clicking ok on alert pop-up the details must be saved to the txt file with seperator by |
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Rules for the password manager
# Length should be minimum of 8
# Contain both uppercase and lowerCase characters
# Should contain alteast one numerical number (0-9)
# Atleast one special character e.g ~!@#$%^&*()_-+=

from random import choice, randint
from tkinter import Tk, Entry, Label, Canvas, PhotoImage, messagebox, Button, END, N, S, E, W
import json
from pyperclip import copy
from os import system

system('clear')


password_special_charac_pattern= '~!@#$%^&*()_-+'
password_number_pattern = '0123456789'
password_charac_pattern = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password_final_pattern = [password_charac_pattern, password_number_pattern, password_special_charac_pattern]
default_email_id = 'biradar.sidduram@gmail.com'

def generate_password():
  random_password = ''
  atleast_one_number = False
  atleast_one_special_char  = False
  
  for _ in range(randint(10,16)):
    random_pattern = choice(password_final_pattern)
    random_charac = choice(random_pattern)
    random_password += random_charac

  for char in random_password:
    if char in password_number_pattern:
      atleast_one_number = True
    if char in password_special_charac_pattern:
      atleast_one_special_char = True

  if not atleast_one_number:
    random_charac = choice(password_number_pattern)
    random_index = randint(0, len(random_password))
    random_password = random_password[0:random_index-1] + random_charac + random_password[random_index+1 :]

  if not atleast_one_special_char:
    random_charac = choice(password_special_charac_pattern)
    random_index = randint(0, len(random_password))
    random_password = random_password[0:random_index-1] + random_charac + random_password[random_index+1 :]

  return random_password


def save_details(name,email,password):
  try:
    with open("data.json") as file:
      data_json = json.load(file)
    if data_json.get(name):
      data_json[name].append({
        "email": email,
        "password": password
      })
    else:
      data_json[name] = [{
        "email": email,
        "password": password
      }]
    json_str = json.dumps(data_json, indent=4)  
    with open("data.json", 'w') as file:
      file.write(json_str)  
  except FileNotFoundError:
    with open("data.json", 'w') as file:
      file.write(json.dumps({}))
      print("Created sample data.json file")
    save_details(name, email, password)      

def set_password():
  password = generate_password()
  password_entry.delete(0, END)
  password_entry.insert(0, password)

def confirm_details():
  website_name = website_name_entry.get()
  email_user_name = email_username_entry.get()
  password = password_entry.get()

  if website_name and email_user_name and password :
    confirm_message = f"These are the details entered:\nEmail/Username: {email_user_name}\nPassword: {password}\nIs this ok?"
    copy(password)
    is_confirmed =  messagebox.askyesno(title=website_name, message=confirm_message)
    if is_confirmed:
      save_details(website_name, email_user_name, password)
      website_name_entry.delete(0, END)
      website_name_entry.insert(0, '')
      password_entry.delete(0, END)
      password_entry.insert(0, '')
  else:
    messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")

def search_details(name=''):
  website_name = website_name_entry.get() or name
  if website_name:
    try:
      with open('data.json') as file:
        data_json = json.load(file)
        if data_json.get(website_name):
          message = ''
          for data in data_json.get(website_name):
            message += f"Email: {data.get('email')}\n Password: {data.get('password')}\n"
          messagebox.showinfo(title=website_name, message=message)  
    except FileNotFoundError:
      with open('data.json', 'w') as file:
        file.write(json.dumps({}))
        print("Created sample data.json file")
    

root = Tk()
root.minsize(width=500, height=500)



lock_image_src = PhotoImage(file='logo.png')
lock_image = Canvas()
lock_image.create_image(150, 100,i = lock_image_src)
lock_image.grid(row=1, column=4, columnspan=5)

website_name_entry = Entry()
email_username_entry = Entry()
password_entry = Entry()
generate_password_button = Button(text='Generate Password', command=set_password)
add_button = Button(text="Add", command=confirm_details)
search_button = Button(text="search", command=search_details)
website_label = Label(text="Website: ", justify="center")
email_username_label = Label(text="Email/Username:", justify="center")
password_label = Label(text="Password:", justify="center")
website_name_entry.bind('<Return>', search_details)
email_username_entry.insert(0, default_email_id)
website_label.grid(row=2,column=3)
website_name_entry.grid(row=2, column=4, sticky=N+S+E+W, pady=5)
search_button.grid(row=2, column=6, columnspan=7, sticky=N+S+E+W, pady=5)
email_username_label.grid(row=3, column=3)
email_username_entry.grid(row=3, column=4, columnspan=6, sticky=N+S+E+W)
password_label.grid(row=4, column=3)
password_entry.grid(row=4, column=4, sticky=N+S+E+W, pady=5)
generate_password_button.grid(row=4, column=6, columnspan=7, sticky=N+S+E+W, pady=5)
add_button.grid(row=5, column=4 , columnspan=6, sticky=N+S+E+W)


root.mainloop()