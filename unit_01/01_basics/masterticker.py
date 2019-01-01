#
#  MasterTicket
#  Python Techdegree
#
#  Created by Dulio Denis on 11/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Buy tickets until there aren't any more left.
#
TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

# Create the calculate_price function. 
# It takes the number of tickets and returns the price.
def calculate_price(number_of_tickets):
  return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code continuously until we run out of tickets
while tickets_remaining > 0:
  # Gather the user's name and assign it to a new variable
  user_name = input("Welcome to MasterTicket. What is your name?  ")

  # Output how many tickets are remaining using the tickets_remaining variable
  
  print("There are {} tickets remaining".format(tickets_remaining))
  
  # Prompt the user by name and ask how many tickets they would like
  try:
    tickets_to_buy = int(input("Hey {} - how many tickets would you like? ".format(user_name)))
  except ValueError:
    print("Tickets should be a number")
  else:
    # Calculate the price: number of tickets * the price - and assign it to a variable
    
    if tickets_to_buy > tickets_remaining:
      print("You can only buy at most {} tickets.".format(tickets_remaining))
    elif tickets_to_buy > 0:
      price = calculate_price(tickets_to_buy)
  
      # output the price to the screen
      print("That will be ${}".format(price))
    
      # Prompt user if they want to proceed: Y/N?
      proceed = input("Would you like to proceed to buy these tickets? (Y/N): ")
    
      # if Y - print out to the screen SOLD!
      if proceed.lower() == 'y':
        print("SOLD!")
        # reduce the tickets_remaining by the number of tickets purchased
        tickets_remaining -= tickets_to_buy
      else:
        # otherwise - thank them by name.
        print("Thank you for visiting {}!".format(user_name))
    else:
      print("You need to buy at least one ticket.")

# Notify tickets are sold out.
if tickets_remaining == 0:
  print("TICKETS SOLD OUT")