# Section 9 Dictionaries and Nesting

# Dictionaries is a key and value pair.

# Syntax is {Key: value}

programming_dictionary = {
  'Bug' : 'An error in program that prevents the program from running as expected.',
  'Function': 'A piece of code that you can easily call over and over again.',
  123: 'Allowing numbers'
}

print(programming_dictionary['Bug'], programming_dictionary[123])
# typo mistake will leads to keyError

programming_dictionary['Loop'] = 'The action of doing something over and over again.'


print(programming_dictionary['Loop'], end='\n\n')

programming_dictionary['Bug'] = 'Bugggggg...'

for key, value in programming_dictionary.items():
  print(key, value)

print("main dictionary", programming_dictionary)

another_dictionary = { key:value for key,value in programming_dictionary.items() }

print("copied dictionary", another_dictionary)

# Grading students based on their scores

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
  score = student_scores[key]
  if score >=91:
    student_grades[key] = 'Outstanding'
  elif score >=81 and score <=90:
    student_grades[key] = 'Exceeds Expectations'
  elif score >= 71 and score <=80:
    student_grades[key] = 'Acceptable'
  else:
    student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting

capitals = {
  "Frnace" : "Paris",
  "Germany" : 'Berlin',
  'India' : 'Delhi'
}

travel_log = {
  "France" : ['Paris', 'Lille', 'Dijon'],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
  "capitals" : capitals,
}

# 
travel_log = [
  {
    "country" : "France",
    "cities_visited": ["Paris", "Lille", 'Dijon'],
    "total_visits": 12
  },
  {
    "country" : 'Germany',
    "cities_visited": ["Berlin", "Hamburg", "Stittgart"],
    "total_visits": 5
  }
]

print(travel_log)

def add_new_country(country, visits, cities):
  travel_log.append({
    'country': country,
    'total_visits': visits,
    'cities_visited': cities
  })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)