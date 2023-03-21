from pandas import read_csv, DataFrame

import csv

another_dict = {}

with open('weather_data.csv') as data_file:
  data = csv.reader(data_file)
  index_count = 0
  keys = []
  for index, items in enumerate(data):
    for item in items:
      if index == 0:
        another_dict[item] = []
        keys.append(item)
      else:
        another_dict[keys[index_count]].append(item)   

      if index_count == len(items)-1:
        index_count = 0
      else:  
        index_count +=1

data = read_csv('weather_data.csv')
print(data['temp'])

data = read_csv('weather_data.csv')
print(data[['temp', 'condition' ,'day']] ,type(data), (data['temp'].to_list()) )

temp_list = (data['temp']).to_list()

print(sum(temp_list)/len(temp_list), data['temp'].mean())

print("Print max value of column temperature :: ", data['temp'].max(), max(temp_list))

print(data[data['temp'] == data['temp'].max()])

print("Condition ", data[data['condition'] == 'Sunny'])

print(data[data['temp'] > data['temp'].min()])

monday = data[data['day'] == 'Monday']

monday_temp_celsius = int(monday['temp']) * 1.8 + 32

print(f"Monday's temperature in celsius {monday_temp_celsius}")


# Create a dataframe from scratch

data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [75,55,65]
}

data = DataFrame(data_dict)

data['Age'] = [24,22,24]

print(data)

# Get a unique squirrel color from the csv and create an another squirrel csv file

data = read_csv('squirrel_new_york_data.csv')
another_data = {
  'Fur Color': [],
  'Count': []
}

for color in data['Primary Fur Color'].unique():
  if type(color) != float:
    count = data[data['Primary Fur Color'] == color]['Primary Fur Color'].count()
    another_data['Fur Color'].append(color)
    another_data['Count'].append(count)

print(another_data)

DataFrame(another_data).to_csv('squirrel_count.csv')