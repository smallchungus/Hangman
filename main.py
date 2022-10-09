"""
So there's a lot to do.
To play hangman first the computer needs to choose a word from a list of words randomly.
Then that words needs to be valid without all the quotation marks and the commas.
Then you need to display the number of letters correctly in hangman style to the user.
Then you need to take in user input until the word is completed or the user doesn't have any lives left.
You also need to print out the letters that the user has chosen so that you don't waste time choosing the same letter.

"""
import random

def play():
    listOfWords = ["string", "super", "duper", "to", "dinosaur"]
    word=random.choice(listOfWords)
    count = 0


    val = input("Enter a letter: ")
    guesses = set()
    correct = list(set())
    correct_guesses = set()

    while correct_guesses != correct:
        # Get input
        guess = input("Guess: ")
        guesses.add(guess)
        correct_guesses = guesses.intersection(correct)

        # Print word status
        placeholder = ' '.join(['%s' for _ in word])
        print(placeholder % tuple([l if l in correct_guesses else '-' for l in word]))
        print("You've guessed: " + ", ".join(guesses))


    for element in range(0, len(word)):
        count += 1

    showUser = "_ "
    print(count * showUser)




play()