
with open('./my_file2.txt', 'r+') as file:
  data = file.read()
  max_score = int(data.split('=').pop())
  max_score+=1
  file.seek(0) 
  file.write(f'max_score={max_score}')
  file.truncate()


with open('/home/siddu/documents/learning/python/Day 24/temp/my_file.txt', 'a+') as file:
  file.seek(0)
  file.truncate()
  file.write('Hello my name is dev_sid')