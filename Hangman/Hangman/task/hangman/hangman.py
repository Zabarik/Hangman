import random

print("H A N G M A N")
languages = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(languages)
guessed_letters = set()
typed_letters = set()
lives = 8
while input('Type "play" to play the game, "exit" to quit: ') == "play":
    while lives > 0:
        print()
        print(''.join([letter if letter in guessed_letters else '-' for letter in random_word]))
        if set(random_word) == guessed_letters:
            print("You guessed the word!")
            print("You survived!\n")
            break
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should print a single letter")
        elif not guess.isalpha() or not guess.islower():
            print("It is not an ASCII lowercase letter")
        elif guess not in random_word and guess not in typed_letters:
            print("No such letter in the word")
            typed_letters.add(guess)
            lives -= 1
        elif guess in typed_letters:
            print("You already typed this letter")
        else:
            typed_letters.add(guess)
            guessed_letters.add(guess)
    else:
        print("You are hanged!\n")
