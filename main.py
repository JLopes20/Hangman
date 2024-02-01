import random
import os
from hangman_art import logo,stages
from hangman_words import word_list


logo = logo
print(logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

chosen_word = random.choice(word_list)
#print(f"Word is: {chosen_word}")

print(stages[6])

display = []
for letter in chosen_word:
    display += "_"
print(" ".join(display))

lives = 6
game_on = False

while not game_on and "_" in display:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed letter: {guess}")
        clear_screen()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        if guess not in chosen_word:
            print(f"{guess} letter is not in the word")
        lives -= 1
        if lives == 0:
            game_on = True
            print("You lose")

    print(" ".join(display))

    if "_" not in display:
        print("You win!")
    print(stages[lives])
