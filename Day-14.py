#Importing
import random
import art
import game_data

#Printing Game Logo from external Python program
print(art.logo)

#Initial starting data
print("\nWelcome to the Higher or Lower Game!\n")

data_length = len(game_data.data)
global score
score = 0
game_end = False

#Person 1 Data function
def person_1(num):
  name = game_data.data[num]["name"]
  desc = game_data.data[num]["description"]
  country = game_data.data[num]["country"]
  followers = game_data.data[num]["follower_count"]
  return {"name": name, "desc": desc, "country": country, "followers": followers}

#Person 2 Data function
def person_2(num):
  name = game_data.data[num]["name"]
  desc = game_data.data[num]["description"]
  country = game_data.data[num]["country"]
  followers = game_data.data[num]["follower_count"]
  return {"name": name, "desc": desc, "country": country, "followers": followers}

#Data Checker function
def checker(choice,p1,p2):
  if p1 > p2 and choice == 1:
    return True
  elif p1 < p2 and choice == 1:
    return False
  elif p2 > p1 and choice == 2:
    return True
  elif p2 < p1 and choice == 2:
    return False

#Game Loop start
while game_end == False:
  number_1 = random.randint(0,(data_length))
  condition = False
  #Assigning 2 unique random numbers
  while condition == False:
    number_2 = random.randint(0,(data_length))
    if number_2 == number_1:
      condition = False
    else:
      condition = True
  print("\nWho/What do you think has more followers on Instagram?\n")
  print(f"\n{person_1(number_1)['name']}, a {person_1(number_1)['desc']} from {person_1(number_1)['country']}\n")
  print(f"\n{art.vs}\n")
  print(f"\n{person_2(number_2)['name']}, a {person_2(number_2)['desc']} from {person_2(number_2)['country']} ?\n")
  user_choice = int(input("\nPlease enter: 1 or 2, for the first or second option respectively\n"))
  if checker(user_choice, person_1(number_1)['followers'], person_2(number_2)['followers']) == True:
    print(f"\nCongratulations! You are correct! {person_1(number_1)['name']} has {person_1(number_1)['followers']} followers; while {person_2(number_2)['name']} has {person_2(number_2)['followers']} followers\n")
    score += 1
    game_end = False
  else:
    print("\nOops! Looks like you guessed wrong! You lose!\n")
    game_end = True

#Final score
print(f"\nYour Final Score is: {score}")
    