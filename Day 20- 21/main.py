# Inheritance in class

class Animal():
  
  def __init__(self, name):
    self.name = name

  def animal_name(self):
    print(f"My name is {self.name}")


class Fish(Animal):
  
  def __init__(self, name):
    super().__init__(name)

  def animal_name(self):
    super().animal_name()
    print("Can do lot more")

fish = Fish("Walle")
fish.animal_name()

# Slicing Lists and Tuples

list_items = [1,2,3,4,5,6,7]

# slice from third pos till end
print(list_items[2:])

print('reverse items', list_items[::-1])