import random


def play_game():
    words = ('python', 'java', 'kotlin', 'javascript')
    random.seed()
    word = list(random.choice(words))
    guessed_word = list("-" * len(word))
    wrong_guesses = set()
    lives = 8

    while lives > 0 and word != guessed_word:
        print()
        print(''.join(guessed_word))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not guess.islower():
            print("Please enter a lowercase English letter")
            continue

        if guess in word:
            if guess in guessed_word:
                print("You've already guessed this letter")
            else:
                for index in range(0, len(word)):
                    if word[index] == guess:
                        guessed_word[index] = guess
        else:
            if guess in wrong_guesses:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                wrong_guesses.add(guess)
                lives -= 1

    print("You survived!" if guessed_word == word else "You lost!")


print("H A N G M A N")
while input('Type "play" to play the game, "exit" to quit: ') == "play":
    play_game()
