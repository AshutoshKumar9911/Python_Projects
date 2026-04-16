import random
import Hangman_stage
import Name_List

# word_list = ["apple", "beautiful", "potato"]
lives = 6

chosen_word = random.choice(Name_List.Name)
print(chosen_word)

display = []
for i in range(len(chosen_word)):
    display += '_'

print(display)

game_over = False

# Now we take input from user
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("You lose!")

    if '_' not in display:
        game_over = True
        print("you win")
    print(Hangman_stage.stages[lives])
