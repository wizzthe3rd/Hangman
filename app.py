import random
import string

from words import words

def getValidWord(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 6

    while len(wordLetters) > 0 and lives > 0:
        print("You have used these letters: ", " ".join(usedLetters))
        print(f"Number of lives = {lives}")

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print("Current word: ", " ".join(wordList))

        usedLetter = input("Enter a letter: ").upper()
        if usedLetter in alphabet - usedLetters:
            usedLetters.add(usedLetter)
            if usedLetter in wordLetters:
                wordLetters.remove(usedLetter)
            else:
                lives -= 1
                print(f"Letter is not present in the word")
        elif usedLetter in usedLetters:
            print("You have already used this letter!")
        else:
            print("Invalid character entered!")

    if lives == 0:
        print(f"You ran out of lives! The word was {word}")
    else:
        print(f"You won, you guessed the word {word}!!")


hangman()