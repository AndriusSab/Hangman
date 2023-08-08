
import random
from typing import List
from words_list import get_random_words_list
from hangman_states import hangman_states
from art import text2art


class HangmanGame:
    def __init__(self):
        self.words_list: List[str] = get_random_words_list()
        self.secret_word: str = random.choice(self.words_list).lower()
        self.guesses: List[str] = []
        self.max_attempts: int = 10
        self.hangman_states: List[str] = hangman_states
        self.current_hangman_state: int = 0

    def print_welcome(self) -> None:
        welcome_text = """
        Welcome to Hangman Game!
       
        """
        formatted_welcome = text2art(welcome_text, font="small")
        print(formatted_welcome)
    
    def display_word(self) -> str:
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def display_hangman(self) -> None:
        print(self.hangman_states[self.current_hangman_state])


    def make_guess(self, guess: str) -> bool:
        guess = guess.lower()
        if guess == self.secret_word:
            self.guesses.append(guess)
            return True
        elif guess in self.guesses:
            return False
        else:
            self.guesses.append(guess)
            if guess not in self.secret_word:
                self.max_attempts -= 1
                self.current_hangman_state += 1
            return False

    def is_game_over(self) -> bool:
        if self.max_attempts <= 0 or self.current_hangman_state >= len(self.hangman_states):
            return True
        if "_" not in self.display_word():
            return True
        return False

    def play(self) -> None:
        self.print_welcome()

        while not self.is_game_over():
            print("\n Attempts left:", self.max_attempts)
            print("\n Word:", self.display_word())
            self.display_hangman()
            guess = input("Guess a letter or word: ").lower()

            if not guess.isalpha():
                print("Please enter letters only.")
                continue

            if len(guess) == 1:
                if guess in self.guesses:
                    print("You've already guessed that letter.")
                    continue
                if guess in self.secret_word:
                    self.make_guess(guess)
                    print("\n Correct guess! Keep it up!")
                else:
                    self.make_guess(guess)
                    print("\n Incorrect guess! Try again")
            elif len(guess) > 1:
                if guess == self.secret_word:
                    self.make_guess(guess)
                    print("\n Congratulations! You've guessed the word:", self.secret_word)
                    break
                else:
                    self.make_guess(guess)
                    print("\n Incorrect guess! Try again")

            if self.is_game_over():
                break
        if "_" not in self.display_word():
            print("\n Congratulations! You've guessed the word:", self.secret_word)
        else:
            print("\n Sorry, you're out of attempts. The word was:", self.secret_word)
            
        play_again = input("\n Do you want to play again? (Y/N): ")
        
        if play_again.upper() == "Y":
            self.__init__()  
            self.play()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
