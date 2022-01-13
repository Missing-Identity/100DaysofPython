#Initial lists, imports, variables and Dicts
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = {
  "Ace": 11,
  "King": 10,
  "Queen": 10,
  "Jack": 10,
  "Ten": 10,
  "Nine": 9,
  "Eight": 8,
  "Seven": 7,
  "Six": 6,
  "Five": 5,
  "Four": 4,
  "Three": 3,
  "Two": 2,
  "One": 1
}
types = ["Hearts", "Clubs", "Spades", "Diamonds"]
numbers = ["Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
user_list = []
user_cards = []
dealer_list = []
dealer_cards = []
play_again = True

#Modules
def assign_card():
  random_value = random.choice(numbers)
  return random_value

def user_deck(num):
  cards["Ace"] = 11
  for i in user_list:
    if int(user_total()) > 20 or i == 11:
      cards["Ace"] = 1
    elif int(user_total()) > 20 and i == 11:
      cards["Ace"] = 1
  user_list.append(cards[num])#Number
  user_cards.append(random.choice(types))#Card Type

def dealer_deck(num):
  cards["Ace"] = 11
  for i in dealer_list:
    if int(dealer_total()) > 20 or i == 11:
      cards["Ace"] = 1
    elif int(dealer_total()) > 20 or i == 11:
      cards["Ace"] = 1
  dealer_list.append(cards[num])
  dealer_cards.append(random.choice(types))

def initial_draw():
  user_deck(assign_card())
  user_deck(assign_card())
  dealer_deck(assign_card())
  dealer_deck(assign_card())

def user_hand():
   print("\nYour hand:- \n")
   for i in range(0, len(user_list)):
     print(f"{user_list[i]} of {user_cards[i]};")

def dealer_hand():
  print("\n\nDealer's hand:- \n")
  for i in range(0, len((dealer_list))-1):
    print(f"{dealer_list[i]} of {dealer_cards[i]};")
  print("?")

def final_dealer_hand():
  print("\nDealer's hand:- \n")
  for i in range(0, len((dealer_list))):
    print(f"{dealer_list[i]} of {dealer_cards[i]};")

def user_total():
  user_sum = 0
  for i in user_list:
    user_sum += i
  return int(user_sum)

def dealer_total():
  dealer_sum = 0
  for i in dealer_list:
    dealer_sum += i
  return int(dealer_sum)


#User Game Start
print(logo)
print("Hello! Welcome to BlackJack!\n")

condition = False
while condition == False:
  play_choice = input("Do you want to play BlackJack? Yes or No:- \n").lower()
  if play_choice == "no":
    play_again = False
    condition = True
    print("Thanks for playing BlackJack!")
  elif play_choice == "yes":
    play_again = True
    condition = True
  else:
    print("Oops! Wrong input! Please try inputing either Yes or No!")
    condition = False

#BlackJack Play Loop
while play_again == True:
  initial_draw()
  user_hand()
  dealer_hand()
  condition = False

  #Checking if initial draw has led to a bust or no
  if int(user_total()) > 21 and int(dealer_total()) < 21:
    condition = True
    print("Looks like its a bust! Sorry! You lose!\n")
  elif int(dealer_total()) > 21 and int(user_total()) < 21:
    condition = True
    print("Looks like the Dealer's busted already! Congratulations! You win!\n")
  elif int(dealer_total()) > 21 and int(user_total()) > 21:
    condition = True
    print("Looks like both of you are busted! Its a draw!")

#Hit or Push
  while condition == False:
    hit_input = input("Do you want to Hit or Push? Enter Hit or Push:- \n").lower()
    if hit_input == "push":
      condition = True
      if int(dealer_total()) <= 17:#If Dealer has <17, has to draw a card if user pushes.
        dealer_deck(assign_card())
      if int(dealer_total()) > 21:
        final_dealer_hand()
        print("Looks like its a dealer bust! You win!\n")
        break
      if int(user_total()) > int(dealer_total()):
        user_hand()
        final_dealer_hand()
        print("Congratulations! You Win!\n")
      elif int(user_total()) < int(dealer_total()):
        user_hand()
        final_dealer_hand()
        print("Sorry! But looks like you lose!\n")
      elif int(user_total()) == int(dealer_total()):
        user_hand()
        final_dealer_hand()
        print("Its a draw!\n")

    elif hit_input == "hit":
      user_deck(assign_card())
      dealer_deck(assign_card())
      if int(user_total()) > 21 and int(dealer_total()) < 21:
        condition = True
        user_hand()
        final_dealer_hand()
        print("Your hit got you busted! You Lose!\n")
      elif int(user_total()) < 21 and int(dealer_total()) > 21:
        condition = True
        user_hand()
        final_dealer_hand()
        print("Your hit got the dealer busted! You Win!")
      elif int(user_total()) > 21 and int(dealer_total()) > 21:
        condition = True
        user_hand()
        final_dealer_hand()
        print("Your hit got both of you busted! Draw!")
      else:
        user_hand()
        dealer_hand()
        condition = False

    
    else:
      print("Wrong input! Please enter 'Hit' or 'PUSH'!\n")
      condition = False
    
  loop_condition = False
  while loop_condition == False:
    user_loop_choice = input("\n \n \n Do you want to play again? Yes or No? \n").lower()
    if user_loop_choice == "yes":
      loop_condition = True
      play_again = True
      user_list = []#Resetting the user and dealer cards
      user_cards = []
      dealer_cards = []
      dealer_list = []
    elif user_loop_choice == "no":
      loop_condition = True
      play_again = False
    else:
      print("Wrong Input! Use either YES or NO!")
      loop_condition = False


print("Thank you for playing BlackJack!")