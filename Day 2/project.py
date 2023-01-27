# Tip calculator
print("Welcome to the tip calculator.")
bill = float( input("What was the total bill? $") )
percentage_tip = int( input("What percentage tip would you like to give? 10, 12, or 15? ") )
persons = int( input("How many people to split the bill? ") )
bill_per_person = round((bill + bill* (percentage_tip/100) )/persons, 2)
print(f"Each person should pay: {bill_per_person}")