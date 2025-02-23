# John Burnson
# CSC500
# Module 6

print()

import sys
import datetime
from datetime import datetime as dt
# Get running date as MONTH D, YYYY
running_date = dt.now().strftime("%B %d, %Y").replace(" 0", " ")

#print('STEP 1: Build the ItemToPurchase class, including default values "none",0,0')
class ItemToPurchase:
  def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='blank'):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  def print_item_cost(self):
    print(self.item_name, self.item_quantity, '@ $' + str(f"{self.item_price:.2f}"), '= $' + str(f"{self.item_quantity * self.item_price:.2f}"))

  def print_item_description(self):
    print(self.item_name + ': ' + self.item_description)

#print('STEP 2: Prompt the user for two items')
#items = [] # initialize list of objects

def get_item_info():
  name = input('\nEnter the item name: ')
  price = float(input('Enter the item price: $'))
  quantity = int(input('Enter the item quantity: '))
  description = input('Enter the item description: ')
  #print()
  print('Item added\n')
  return ItemToPurchase(name, price, quantity, description)

#print('STEP 3: Output the total cost')
#print('Total: $' + str(f"{sum(c.item_quantity * c.item_price for c in items):.2f}"))

# New for Module6:
#print('STEP 4: Build the ShoppingCart class')
# https://stackoverflow.com/questions/9751554/list-as-a-member-of-a-python-class-why-is-its-contents-being-shared-across-all
# https://stackoverflow.com/questions/1680528/how-to-avoid-having-class-data-shared-among-instances?noredirect=1&lq=1
# https://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python
# Using class members to give default values works very well just so long as you are careful only to do it with immutable values. If you try to do it with a list or a dict that would be pretty deadly.
class ShoppingCart:
  def __init__(self, customer_name="none", current_date="January 1, 2020"): # , cart_items=[] Don't do this here!
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = [] # cart_items

  def add_item(self, item):         # Has parameter ItemToPurchase
    self.cart_items.append(item)

  def remove_item(self, item_name): # Has a string (an item's name) parameter.
    pass # TK

  def modify_item(self, item):      # Has parameter ItemToPurchase
    pass # TK

  def get_num_items_in_cart(self):  # Has no parameters.
    #return len(self.cart_items)
    #return sum(self.cart_items.item_quantity)
    return sum(c.item_quantity for c in self.cart_items)

  def get_cost_of_cart(self):       # Has no parameters.
    pass # TK

  def print_total(self):            # If cart is empty, output SHOPPING CART IS EMPTY
    print()
    print(self.customer_name + "'s Shopping Cart - " + self.current_date)
    if self.get_num_items_in_cart() == 0:
      print("SHOPPING CART IS EMPTY")
    else:
      print("Number of items: " + str(self.get_num_items_in_cart()))
      # Print the other details
      for index, value in enumerate(self.cart_items):
        value.print_item_cost()
      print('Total: $' + str(f"{sum(c.item_quantity * c.item_price for c in self.cart_items):.2f}"))
    print()

  def print_descriptions(self):     # If cart is empty, output SHOPPING CART IS EMPTY
    print()
    print(self.customer_name + "'s Shopping Cart - " + self.current_date)
    if self.get_num_items_in_cart() == 0:
      print("SHOPPING CART IS EMPTY")
    else:
      print("Item Descriptions")
      for index, value in enumerate(self.cart_items):
        value.print_item_description()
    print()

#sys.exit()

def centered_string(string_to_be_centered='', centering_width=50):
  # If a function lacks a return statement, or if it has a return statement without a value, it returns None.
  return string_to_be_centered.center(centering_width)

def main():
    print("\n*** Main Start ***")

    # Create your cart
    my_cart = ShoppingCart() # customer_name='JB', current_date=running_date)

#print('STEP 5: Implement the print_menu() function')
    # https://stackoverflow.com/questions/27161537/using-class-instance-as-a-function-argument
    def print_menu(cart):           # Has a ShoppingCart parameter.
      while True:
        print(centered_string("MENU"))
        print(centered_string("a - Add item to cart"))
        print(centered_string("r - Remove item from cart"))
        print(centered_string("c - Change item quantity"))
        print(centered_string("i - Output items' descriptions"))
        print(centered_string("o - Output shopping cart"))
        print(centered_string("q - Quit"))

        option_chosen = input(centered_string('Choose an option:'))

        match option_chosen:
          case 'a':
              my_cart.add_item(get_item_info())
          case 'r':
              print('Code to be completed in later steps\n') #my_cart.remove_item('')
          case 'c':
              print('Code to be completed in later steps\n') #my_cart.change_item_quantity('')
#print('STEP 6: Implement Output item's description menu option')
          case 'i':
              my_cart.print_descriptions()
#print('STEP 6: Implement Output shopping cart menu option')
          case 'o':
              my_cart.print_total()
          case 'q':
              break
          case _:
              print('Invalid option. Try again\n')

    print_menu(my_cart)
    print("*** Main End ***")

# https://stackoverflow.com/questions/22492162/understanding-the-main-method-of-python
if __name__ != '__main__':
    print("This program is being imported from another module, so do not run main().")
else:
    print("This program is being executed as __main__")
    main()
