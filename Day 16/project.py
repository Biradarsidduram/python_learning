# Coffee Machine Using OOP

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

while True:
  choice =  input(f"What would you like ? ({menu.get_items()}) ")
  if choice == 'off':
    break
  elif choice == 'report':
    coffeeMaker.report()
  else:
    menu_item = menu.find_drink(choice)
    if menu_item:
      if coffeeMaker.is_resource_sufficient(menu_item) and moneyMachine.make_payment(menu_item.cost):
          coffeeMaker.make_coffee(menu_item)