# Section 10 Funtions with Outputs

def my_function():
  result = 3 * 2
  return result

print(my_function())

def format_name(f_name, l_name):
  return f"{f_name.title()} {l_name.title()}"
  
full_name = format_name('siddu', 'ram')

print(full_name)

# Multiple return values


def format_name(f_name, l_name):
  """
    Takes a first and last name format it to return the title case version of the name if .
  """
  if f_name == '' or l_name == '':
    return 
  return f"Result: {f_name.title()}{l_name.title()}"

print(format_name(input("What is your first name ? "), input("What is your last name ? ")))

# A program which get days of month from year

def is_leap(year):
  """ A function which check whether a year is a leap year or not 
  """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  is_leap_year =  is_leap(year)
  if is_leap_year and month ==2:
    return month_days[month-1] + 1
  else:
    return month_days[month-1]  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)