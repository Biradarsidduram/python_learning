# Day 5 For loops, Range and Code Blocks

# Average Height of the student
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
no_of_students =0

for student in student_heights:
  total_height+=student
  no_of_students+=1

average_height = round(total_height/no_of_students)
print(average_height)


# Maximum score within the list
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0

for score in student_scores:
  if max_score <= score:
    max_score = score
print(f"The highest score in the class is: {max_score}")

# range function

#Write your code below this row 👇

sum_of_even = 0 

for num in range(2,101):
  if num % 2 == 0:
    sum_of_even+=num
print(sum_of_even)

#Write your code below this row 👇

for num in range(1, 101):
  if num % 15 ==0:
    print("FizzBuzz")
  elif num % 5 ==0:
    print("Buzz")
  elif num % 3 ==0:
    print("Fizz")
  else:
    print(num)