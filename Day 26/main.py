# List Comprehension

from pandas import DataFrame

from random import randint

numbers = [1,2,3]

new_list = []

for number in numbers:
  new_list.append(number + 1)


print(new_list)

print("let's use list comprehension")

new_list = [ num+1 for num in numbers ]

print(new_list)

name = "Angela"

new_list = [ letter for letter in name ]

print(new_list)

print(''.join(new_list))

tuple_list = (1,2,3)

new_tuple_list = ( num + 2 for num in tuple_list )

print(tuple_list, new_tuple_list, new_list)

for item in new_tuple_list:
  print(item) 

lists = [ num * 2 for num in range(1,5) ]

print(lists)

dict_temp  = {
  'x':2,
  'y':3
}

# dictionary comprehension

new_dict_temp = { key:value+2 for key, value in dict_temp.items() }

print(new_dict_temp)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [ name for name in names if len(name) < 5 ]

print(short_names)

long_names = [ name for name in names if len(name) > 5 ]

print(long_names)

numbers = [1,1,2,3, 5,8,13,21,34,55]

even_numbers = [ num for num in numbers if num %2 == 0]

print(even_numbers)

# Dictionary Comprehension 

students_score = { name: randint(1, 100) for name in names }

print("students scores are ", students_score)

passed_students = { name:score for name,score in students_score.items() if score >= 60 }

print("Passed students are ", passed_students)

# Conver the sentence into a dictionary where each word is a key and it's length a value

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = { word : len(word) for word in sentence.split(' ') }

print(result)

# Convert weather data from celsius to fahrenheit

weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24,
}

weather_f = { day: round(temperature* 1.8 + 32, 2) for (day, temperature) in weather_c.items() }

print(weather_f)

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score" : [56, 76, 98]
}

for key, value in student_dict.items():
  print(key, value)

student_dataframe = DataFrame(student_dict)

for index, row in student_dataframe.iterrows():
  if row.student == 'Angela':
    print('Angela\'s sore is ', row.score)
