#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0  # Initialize the amount to zero
    self.discount = discount
    self.items = []
    self.last_transaction_amount = 0  #Track the last added amount 

  def add_item(self, title, price, quantity=1):
    # Add the item's cost to the total and save the transaction amount
    self.total += price * quantity
    self.last_transaction_amount = price * quantity

    # Add the item title to the list once per quantity
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):

    # Apply discount if available and print updated total
    if self.discount > 0:
      discount_amount = self.total * self.discount / 100
      self.total = self.total - discount_amount
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      # Print this statement if there is no discount to be applied
      print("There is no discount to apply.")

  def void_last_transaction(self):

    # Subtract the last transaction from the total
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0  #Then reset the last transaction

  def get_items(self):

    #Return the list of added items
    return self.items


