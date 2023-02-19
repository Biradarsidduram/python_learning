from turtle import Turtle, Screen
from prettytable import PrettyTable

# Object Oriented Programming

# My first class in python
class Dog:
  pass

dog = Dog()

print(dog)

class AnotherDog:
  attr = 'Mammal'  #this attribute is assigned to the class and it's class attribute not object attribute

  def __init__(self, name = '') -> None:
    if name:
      self.name = name
    else:
      self.name = 'mark'
  
  def bark(self) -> None:
    print(f"Bow Bow Boooww my name is {self.name} -> ", self.attr)   


another_dog = AnotherDog("Snoopie")
another_dog.bark()


print(another_dog.attr)

mark_dog = AnotherDog()

mark_dog.bark()

print(mark_dog.__class__.attr)

class Person():
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber
  def display(self):
    print(self.name)
    print(self.idnumber)
  def details(self):
    print("My name is {}".format(self.name))
    print("My idNumbers is {}".format(self.idnumber))

class Employee(Person):
  
  def __init__(self, name, idnumber, salary, post):
    Person.__init__(self,name,idnumber)
    self.salary = salary
    self.post = post

  def details(self):
    print("My name is {}".format(self.name))
    print("IdNumbers: {}".format(self.idnumber))
    print("Post: {}".format(self.post))   

ab = Person("Ronit",23)

ab.details()

a = Employee('Rahul', 22, '1000', 'Intern')

a.details()

class Bird():
  def intro(self) -> None:
    print("There are many types of birds")
  def flight(self) -> None:
    print("Most of the birds fly but some cannot")

class Sparrow(Bird):
  def flight(self):
    print("Sparrows can fly")

class Ostrich(Bird):
  def flight(self):
    print("Ostrich cannot fly")


sparrow = Sparrow()

sparrow.intro()
sparrow.flight()

ostrich = Ostrich()
ostrich.intro()
ostrich.flight()


class Base():

  def __init__(self, name, identifier) -> None:
    self.__name = name
    self.identifier = identifier

  def print_details(self):
    print("My name is {} and my id is {}".format(self.name, self.identifier))

class Derive(Base):

  def __init__(self, name, identifier):
    Base.__init__(self, name, identifier)

  def print_details(self):
    print("Calling private number of base class : {}".format(self.identifier))

obj1 = Derive("Jonita", 19)

obj1.print_details()

# PrettyTable Plugin

table = PrettyTable()

print(table.align)


table.align = 'l'

table.add_column('Pokemon Name', ['Pickachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'water', 'fire'])

print(table)

# Turtle API

timmy = Turtle()
timmy.color('black')

timmy.shape("turtle")

timmy.forward(150)
timmy.right(90)
timmy.forward(30)
timmy.right(90)
timmy.forward(150)
timmy.right(90)
timmy.forward(30)


my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()
