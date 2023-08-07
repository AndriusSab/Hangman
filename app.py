import random
from typing import List
from words_list import get_random_words_list

class HangmanGame:
    def __init__(self):
        self.words_list: List[str] = get_random_words_list()
        self.secret_word: str = random.choice(self.words_list).lower()
        self.guesses: List[str] = []
        self.max_attempts: int = 6

    def display_word(self) -> str:
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def make_guess(self, letter: str) -> bool:
        letter = letter.lower()
        if letter in self.guesses:
            return False
        self.guesses.append(letter)
        self.max_attempts -= 1
        return True

    def is_game_over(self) -> bool:
        if self.max_attempts <= 0:
            return True
        if "_" not in self.display_word():
            return True
        return False

    def play(self) -> None:
        print("Welcome to Hangman!")

        while not self.is_game_over():
            print("\nAttempts left:", self.max_attempts)
            print("Word:", self.display_word())
            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if not self.make_guess(guess):
                print("You've already guessed that letter.")

            if self.is_game_over():
                break

        if "_" not in self.display_word():
            print("Congratulations! You've guessed the word:", self.secret_word)
        else:
            print("Sorry, you're out of attempts. The word was:", self.secret_word)

if __name__ == "__main__":
    game = HangmanGame()
    game.play()

