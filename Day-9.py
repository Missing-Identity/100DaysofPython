from replit import clear#importing clear command for replit
import art#Importing ASCII art from another python program
print(art.logo)
bidders = {}
loop = True
highest_bid = 0
highest_name = " "
while loop == True:
  name = input("Please enter your name: ")
  bid = float(input("How much do you want to bid?"))
  bidders[name] = bid
  for name in bidders:
    if bidders[name] > highest_bid:
      highest_bid = bidders[name]
      highest_name = name
    else:
      highest_bid = highest_bid
      highest_name = highest_name
    
  condition = False
  while condition == False:
    user_input = input("Are there any other bidders? Yes or No?").lower()
    if user_input == "yes" or user_input == "no":
      condition = True
    else:
      condition = False
      print("Incorrect input! Please enter Yes or No!")
  if user_input == "no":
    loop = False
  else:
    loop = True
    clear()
print(f"The Highest Bidder is: {highest_name}, with a bid of: {highest_bid}")