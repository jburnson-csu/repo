# John Burnson
# CSC500
# Module 4

print()

# STEP 1
print('STEP 1: Build the ItemToPurchase class, including default values "none",0,0')
print()

# You can assign any type of value to a class attribute, as with any other variable.
class ItemToPurchase:
  def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity

  def print_item_cost(self):
    print(self.item_name, self.item_quantity, '@ $' + str(f"{self.item_price:.2f}"), '= $' + str(f"{self.item_quantity * self.item_price:.2f}"))

# Print example of print_item_cost() for default values
print('Example of method print_item_cost(), using default values:')
ItemToPurchase().print_item_cost()

print()

# STEP 2
print('STEP 2: Prompt the user for two items')
print()
items = [] # initialize list of objects

def get_item_info():
  name = input('Enter the item name: ')
  price = float(input('Enter the item price: $'))
  quantity = int(input('Enter the item quantity: '))
  print()
  return ItemToPurchase(name, price, quantity)

print('Item 1')
items.append(get_item_info()) # ItemToPurchase('Chocolate Chips', 3, 1)
print('Item 2')
items.append(get_item_info()) # ItemToPurchase('Bottled Water', 1, 10)

# STEP 3
print('STEP 3: Output the total cost')
print()
print('TOTAL COST')
# To get the index and value of each element, you can use the enumerate() function.
for index, value in enumerate(items):
  value.print_item_cost()

# Use a generator expression
# https://stackoverflow.com/questions/10879867/sum-average-an-attribute-of-a-list-of-objects
# Lets say I have class C which has attribute a. What is the best way to get the sum of a from a list of C in Python?
print('Total: $' + str(f"{sum(c.item_quantity * c.item_price for c in items):.2f}"))

# End
