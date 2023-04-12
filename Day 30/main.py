# Errors, Exceptions and Saving JSON Data

from os import system

system('clear\n echo hello world ')

# Index out of range error

# list_items = [1,2,3]

# print(list_items[3])

# # Key Not found error

# dict_items = {
#   "key" : "value"
# }

# print(dict_items["key_does_not_exists"])

# # Type mismatch error

# type_error = "str" + 3

# print(type_error)


try:
    with open("file.txt", 'r+') as file:
        print(file.read())
    list_items = [1, 2, 3]
    print(list_items[3])

except FileNotFoundError:
    file = open("file.txt", 'w+')
    file.write("Something")
    file.close()
    print("File not found buddy")

except IndexError:
    print("Index out of range Error")

value = int(input("Please enter value less than 50 "))

try:
    if value > 50:
        raise ValueError(f"Value {value} entered is greater than 50")
    else:
        print("Entered value is ", value)
except Exception as error:
    print("error ::", error)
