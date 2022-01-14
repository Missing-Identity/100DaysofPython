import random

logo = '''
 _______               ___.                    ________                            .__                   ________                     ._.
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____| |
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ |
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/\|
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >_
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/\/
'''
print(logo+"\n")
print("Welcome to the Number Guessing Game!\n")
chosen_number = random.randint(1,100)
win_status = False
condition = False
while condition == False:
  difficulty = input("What difficulty do you want to play in? 'Easy' or 'Hard'?:-\n").lower()
  if difficulty == "easy":
    condition = True
    attempts = 10
  elif difficulty == "hard":
    condition = True
    attempts = 5
  else:
    condition = False
    print("Please enter a valid difficulty!\n")

def user_input():
  guess = int(input("Enter a guess:-"))
  return guess

def comparision(guess):
  global attempts
  if guess > chosen_number:
    print("Too High!")
    attempts -= 1
    print(f"Total attempts left: {attempts}")
  elif guess < chosen_number:
    print("Too Low!")
    attempts -= 1
    print(f"Total attempts left: {attempts}")
  else:
    print("You guessed correctly! You Win!")
    global win_status
    win_status = True
    print(f"The number to be guessed was: {chosen_number}")

while attempts > 0:
  if win_status == True:
    break
  guess = user_input()
  comparision(guess)

if win_status == False:
  print(f"Looks like you lose! The correct answer was: {chosen_number}")
