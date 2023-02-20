# Day 17 Goals, creating classes and quiz game

class Bottle():
  def __init__(self, capacity, name):
    self.capacity = capacity
    self._name = name

  # here print_details is the methods to the class and we can call on it to perform operations on the attributes data

  def print_details(self):
    print("The bottle name is {} which holds capacity of {}ml.".format(self._name, self.capacity))

bottle = Bottle(capacity=900, name = 'Tupperware')

bottle.print_details()

bottle._name = 'Milton'

bottle.print_details()


class User():

  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.followers = 0
    self.following = 0
  
  def print_details(self): 
    print("User name is {} and his Id is {},  followers count is {}, following count is {} ".format(self.name, self.id, self.followers, self.following)) 

  def follow(self, user):
    user.followers += 1
    self.following += 1

user_1 = User("John", 8)
user_2 = User('Jane', 6)

user_1.follow(user_2)

user_1.print_details()
user_2.print_details()

 