# John Burnson
# CSC500
# Module 5

print()

import sys
import calendar

# Part 1
print('*** Part 1 ***')

# Describe the task
print('This program uses nested loops to collect data and calculate the average rainfall over a period of years.')

# Input the number of years
rainfall_years = -1
while True:
  try:
    rainfall_years = int(input('Enter the number of years of rainfall (mininum 1): '))
  except ValueError:
    # Code to handle the ValueError
    print('Invalid input. Please enter a valid number.')
  if rainfall_years >= 1:
    break
  print('Please re-try with a proper number of years.')
  print()

print('For each month, enter the inches of rainfall.')
rainfall_for_period = 0
for y in range(rainfall_years):
  print('   Year',y+1)
  for m in range(12):
    #print(' ',calendar.month_name[m+1]) # m+1)
    rainfall_for_month = -1
    while True:
      try:
#       rainfall_for_month = float(input('    Enter the number of inches of rainfall (mininum 0): '))
#       rainfall_for_month = float(input('  '+calendar.month_name[m+1]+': '))
#        rainfall_for_month = float(input(f"{'  '+calendar.month_name[m+1] : <11}" +': '))
        rainfall_for_month = float(input(f"{'  '+calendar.month_name[m+1] +': ' : <13}"))
      except ValueError:
        # Code to handle the ValueError
        print('Invalid input. Please enter a valid number.')
      if rainfall_for_month >= 0:
        break
      print('Please re-try with a proper number of inches.')
    rainfall_for_period = rainfall_for_period + rainfall_for_month

print()
print('Length of period:',rainfall_years*12,'months')
print('Total rainfall:',rainfall_for_period,'inches')
print('Average monthly rain:',rainfall_for_period/(rainfall_years*12),'in.')

print()

#sys.exit()

# Part 2
print('*** Part 2 ***')

# Describe the task
print('This program calculates points based on the number of books purchased in a month from the CSU Global Bookstore.')

# Input the number of books purchased
books_purchased_this_month = -1
while True:
  try:
    # When prompting the user for input, a ValueError can occur. This commonly happens when using int() or float() to convert user input.
    # Code that could raise a ValueError
    books_purchased_this_month = int(input('Enter the number of books that you have purchased this month (minimum 0): '))
  except ValueError:
    # Code to handle the ValueError
    print('Invalid input. Please enter a valid number.')
  if books_purchased_this_month >= 0:
    break
  print('Please re-try with a proper number of books.')
  print()

# Starting with Python 3.10, there is a “match” statement to implement case statements with boolean conditions.
# https://metaschool.so/articles/python-switch-case
# We can return multiple values from a function in a tuple:
# https://note.nkmk.me/en/python-function-return-multiple-values/
def calculate_rewards(books):
    match books:
        case _ if books >= 8:
            return 60, 'You are at the highest tier of award.'
        case _ if books >= 6:
            return 30, 'The next-highest tier is 8 books.'
        case _ if books >= 4:
            return 15, 'The next-highest tier is 6 books.'
        case _ if books >= 2:
            return  5, 'The next-highest tier is 4 books.'
        case _:
            return  0, 'The next-highest tier is 2 books.'

print('Points awarded:', calculate_rewards(books_purchased_this_month)[0])

# Also notify the user of the next-higher tier of award:
print(calculate_rewards(books_purchased_this_month)[1])

# End
