# Coffee Machine Project


from data import MENU, resources

def check_resources(resources, menu_item):
  for ingredient,quantity in menu_item['ingredients'].items():
    if resources[ingredient] < quantity:
      print(f"Sorry there is not enough {ingredient}.")
      return False
  return True

def get_coffee_to_constumer(resources, menu_item):
  # delete the required menu item resources from the resources
  for ingredient,quantity in menu_item['ingredients'].items():
    resources[ingredient]-=quantity


def coffee_machine():
  coffe_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
  menu_item = MENU[coffe_type]
  is_resources_available =  check_resources(resources, menu_item)
  if not is_resources_available:
    coffee_machine()
    return
  print(f"The price of {coffe_type} is {menu_item['cost']}")
  print("Please insert coins.")
  quarters = int( input("how many quarters?: ") )
  dimes = int( input("how many dimes?: ") )
  nickles = int( input("how many nickels?: "))
  pennies = int( input("how many pennies?: ") )
  total_amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
  price = menu_item['cost']
  if total_amount >= price:
    remaining_amount = round(total_amount - price, 2)
    get_coffee_to_constumer(resources, menu_item)
    if remaining_amount > 0:
      print(f"Here is ${remaining_amount} in change.")
    print(f"Here is your {coffe_type}. Enjoy!")
  else:
    print(f"Sorry that's not enough money, Money refunded {total_amount}")
  coffee_machine()


coffee_machine()    