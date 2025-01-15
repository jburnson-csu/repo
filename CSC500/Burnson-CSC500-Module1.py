# John Burnson
# CSC500
# Module 1

# Part 1
print()
print('This program finds the ADDITION and SUBTRACTION of two numbers.')

# Ask the user to input two numbers (num1 and num2)...
num1 = int(input('Enter first number:  '))
num2 = int(input('Enter second number: '))

# Given those two numbers, add them together to find the output...
print('Sum:       ',num1,'+',num2,'=',num1 + num2)

# Also, subtract the two numbers to find the output.
print('Difference:',num1,'-',num2,'=',num1 - num2)

print()

# Part 2
print('This program finds the MULTIPLICATION and DIVISION of two numbers.')
print("  Note: If the second number is 0, the quotient can't be calculated!")

# Ask the user to input two numbers (num1 and num2)...
num1 = int(input('Enter first number:  '))
num2 = int(input('Enter second number: '))

# Given those two numbers, multiply them together to find the output...
print('Product:   ',num1,'*',num2,'=',num1 * num2)

# Also, divide num1/num2 to find the output.
print('Quotient:  ',num1,'/',num2,'= ', end='')
print(num1 / num2)
print('(The quotient shows up to 16 digits to the right of the decimal.)')

# End
