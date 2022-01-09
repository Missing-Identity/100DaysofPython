import hangman_words
import random
import hangman_art
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Importing Logo
print(f"{hangman_art.logo}")
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"

counter = 0
guessed_list = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Telling user if their guessed word was already guessed or no.
    if guess in guessed_list:
      print(f"Your guess: {guess}, was already guessed earlier! Please try another letter!")
    guessed_list.append(guess)
    #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #Checking if user is wrong.
    if guess not in chosen_word:
        #Alerting User that their guess is not in the word
        print(f"Your guess: {guess}, is not in the word!\nYou lose one life!\n")
        lives -= 1
        print(f"Remaining lives: {lives}")
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!")
            print(f"The word you had to guess was: {chosen_word.upper()}!")
    #Joining all the elements in the list and turning it into a String. Basically appending list items to a blank space(For clarity) and making it a string(To remove the '' and [])
    print(f"{' '.join(display)}")

    #Checking if user got all the words or no
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    #Importing hangman_art stages
    print(hangman_art.stages[lives])