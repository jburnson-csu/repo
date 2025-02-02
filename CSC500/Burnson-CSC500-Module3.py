# John Burnson
# CSC500
# Module 3

print()

# Part 1
print('*** Part 1 ***')

# Set the constants
tip_rate = 18
tax_rate = 7

# Describe the task
print('This program calculates the total amount of a meal with a tip of {}% and a tax of {}%.'.format(tip_rate, tax_rate))

# Input the food charge
food_charge = float(input('Enter the charge for the food: $'))

# Calculate the tip and tax
food_charge_tip = round(tip_rate/100 * food_charge,2)
food_charge_tax = round(tax_rate/100 * food_charge,2)

# Display each of the amounts and the total price
print()
print(f"{f'${food_charge:,.2f}':>10}  Food charge")
print(f"{f'${food_charge_tip:,.2f}':>10}  Tip @ {tip_rate}%")
print(f"{f'${food_charge_tax:,.2f}':>10}  Tax @ {tax_rate}%")
print(f"{f'=========':>10}  ============")
print(f"{f'${food_charge + food_charge_tip + food_charge_tax:,.2f}':>10}  Total charge")

print()

# Part 2
print('*** Part 2 ***')

# Describe the task
print('This program shows the time on a 24-hour clock in a chosen number of hours from now.')

# Input the time now (in hours)
current_time_on_24_hour_clock = -1
while True:
  current_time_on_24_hour_clock = int(input('Enter the current time, in hours (from 0-23): '))
  if 0 <= current_time_on_24_hour_clock <= 23:
    break
  print('Please re-try with a proper number of hours.')

# Input the number of hours to wait for the alarm
print()
integer_hours_to_wait = -1
while True:
  integer_hours_to_wait = int(input('Enter an integer number of hours to wait (minimum 0): '))
  if integer_hours_to_wait >= 0:
    break
  print('Please re-try with a proper number of hours.')

# Display the time when the alarm goes off. We can use the modulus function.
print()
print('  {} hours after a time of {}, a 24-hour clock will read {}.'.format(integer_hours_to_wait, current_time_on_24_hour_clock, (current_time_on_24_hour_clock + integer_hours_to_wait) % 24))

print('  Also, the clock will have encountered a new day {} times.'.format((current_time_on_24_hour_clock + integer_hours_to_wait) // 24))

# End
