import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to Rock, Paper, Scissors!\n")
choices = [rock, paper, scissors]
cpuchoice = choices[random.randint(0,2)]
userchoice = input("What do you want to pick? Rock, Paper or Scissors?").lower()
if userchoice == "paper":
  userchoice = paper
  print(f"You chose {userchoice}")
  if cpuchoice == rock:
    print(f"Computer chose Rock. \n {cpuchoice}\n YOU WIN!")
  elif cpuchoice == scissors:
    print(f"Computer chose Scissors. \n {cpuchoice}\n YOU LOSE!")
  else:
    print(f"Computer chose {cpuchoice}\n DRAW!")
elif userchoice == "rock":
  userchoice = rock
  print(f"You chose {userchoice}")
  if cpuchoice == scissors:
    print(f"Computer chose Scissors. \n {cpuchoice}\n YOU WIN!")
  elif cpuchoice == paper:
    print(f"Computer chose Paper. \n {cpuchoice}\n YOU LOSE!")
  else:
    print(f"Computer chose {cpuchoice}\n DRAW!")
elif userchoice == "scissors":
  userchoice = scissors
  print(f"You chose {userchoice}")
  if cpuchoice == paper:
    print(f"Computer chose Paper. \n {cpuchoice}\n YOU WIN!")
  elif cpuchoice == rock:
    print(f"Computer chose Rock.\n {cpuchoice}\n YOU LOSE!")
  else:
    print(f"Computer chose {cpuchoice}\n DRAW!")
else:
  print("Oops! Wrong Choice!")