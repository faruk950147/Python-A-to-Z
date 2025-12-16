import random
import os

# class HangmanGame:
#     HANGMAN_PICS = [
#         """
#          -----
#          |   |
#              |
#              |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#              |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#          |   |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|   |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#         /    |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#         / \\  |
#              |
#         --------
#         """
#     ]

#     def __init__(self, word_list):
#         self.word_list = word_list

#     def play(self):
#         self.word = random.choice(self.word_list).lower()
#         self.guessed_letters = set()
#         self.wrong_guesses = set()
#         self.attempts = 6

#         print("Welcome to Hangman!")
#         print(f"The word has {len(self.word)} letters.")

#         while self.attempts > 0:
#             display_word = "".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
#             print("\n" + self.HANGMAN_PICS[len(self.wrong_guesses)])
#             print(f"Word: {display_word}")
#             print(f"Wrong guesses: {', '.join(sorted(self.wrong_guesses))}")

#             if "_" not in display_word:
#                 print(f"\nCongratulations! You guessed the word: {self.word}")
#                 break

#             guess = input("Guess a letter: ").lower()

#             if not guess.isalpha() or len(guess) != 1:
#                 print("Please enter a valid single letter.")
#                 continue

#             if guess in self.guessed_letters or guess in self.wrong_guesses:
#                 print("You already guessed that letter.")
#                 continue

#             if guess in self.word:
#                 self.guessed_letters.add(guess)
#                 print("Correct!")
#             else:
#                 self.wrong_guesses.add(guess)
#                 self.attempts -= 1
#                 print(f"Wrong! Attempts left: {self.attempts}")

#         else:
#             print(self.HANGMAN_PICS[-1])
#             print(f"\nGame Over! The word was: {self.word}")

#         # Play again option
#         again = input("\nDo you want to play again? (y/n): ").lower()
#         if again == "y":
#             self.play()
#         else:
#             print("Thanks for playing! Goodbye.")

# if __name__ == "__main__":
#     word_list = ["apple", "banana", "cherry", "date", "elderberry"]
#     game = HangmanGame(word_list)
#     game.play()

# class AdvancedHangman:
#     HANGMAN_PICS = [
#         """
#          -----
#          |   |
#              |
#              |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#              |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#          |   |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|   |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#              |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#         /    |
#              |
#         --------
#         """,
#         """
#          -----
#          |   |
#          O   |
#         /|\\  |
#         / \\  |
#              |
#         --------
#         """
#     ]

#     WORDS = {
#         "apple": "A type of fruit",
#         "banana": "A yellow long fruit",
#         "cherry": "Small red fruit often on top of desserts",
#         "date": "Sweet fruit from a palm tree",
#         "elderberry": "Dark berry used in syrups"
#     }

#     def __init__(self):
#         self.score = 0

#     def choose_word(self, difficulty):
#         words = list(self.WORDS.keys())
#         if difficulty == "easy":
#             words = [w for w in words if len(w) <= 5]
#         elif difficulty == "medium":
#             words = [w for w in words if 5 < len(w) <= 7]
#         else:  # hard
#             words = [w for w in words if len(w) > 7]
#         return random.choice(words)

#     def play(self):
#         print("Welcome to Advanced Hangman!")
#         difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
#         self.word = self.choose_word(difficulty)
#         self.hint = self.WORDS[self.word]
#         self.guessed_letters = set()
#         self.wrong_guesses = set()
#         self.attempts = 6

#         print(f"The word has {len(self.word)} letters. Hint: {self.hint}")

#         while self.attempts > 0:
#             display_word = "".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
#             print("\n" + self.HANGMAN_PICS[len(self.wrong_guesses)])
#             print(f"Word: {display_word}")
#             print(f"Wrong guesses: {', '.join(sorted(self.wrong_guesses))}")
#             print(f"Score: {self.score}")

#             if "_" not in display_word:
#                 print(f"\nYou guessed the word: {self.word}")
#                 self.score += 10 + len(self.word) - len(self.wrong_guesses)
#                 print(f"Your score: {self.score}")
#                 break

#             guess = input("Guess a letter: ").lower()
#             if not guess.isalpha() or len(guess) != 1:
#                 print("Enter a valid single letter.")
#                 continue
#             if guess in self.guessed_letters or guess in self.wrong_guesses:
#                 print("You already guessed that letter.")
#                 continue

#             if guess in self.word:
#                 self.guessed_letters.add(guess)
#                 print("Correct!")
#             else:
#                 self.wrong_guesses.add(guess)
#                 self.attempts -= 1
#                 print(f"Wrong! Attempts left: {self.attempts}")

#         else:
#             print(self.HANGMAN_PICS[-1])
#             print(f"\nGame Over! The word was: {self.word}")
#             print(f"Your score: {self.score}")

#         again = input("\nPlay again? (y/n): ").lower()
#         if again == "y":
#             self.play()
#         else:
#             print("Thanks for playing! Goodbye.")

# if __name__ == "__main__":
#     game = AdvancedHangman()
#     game.play()



# =============== class WordGuessGame ===================


class WordGuessGame:
    HANGMAN_PICS = [
        """
        +---+
            |
            |
            |
            ===""",
        """
        +---+
        O   |
            |
            |
            ===""",
        """
        +---+
        O   |
        |   |
            |
            ===""",
        """
        +---+
        O   |
        /|   |
            |
            ===""",
        """
        +---+
        O   |
        /|\\  |
            |
            ===""",
        """
        +---+
        O   |
        /|\\  |
        /    |
            ===""",
        """
        +---+
        O   |
        /|\\  |
        / \\  |
            ===""",
    ]

    def __init__(self, dictionary_file="dictionary.txt", max_attempts=6):
        self.dictionary_file = dictionary_file
        self.max_attempts = max_attempts
        self.words = self.load_dictionary()
        self.score = {"wins": 0, "losses": 0}

    def load_dictionary(self):
        if os.path.exists(self.dictionary_file):
            with open(self.dictionary_file, "r") as file:
                words = file.read().splitlines()
            return words
        else:
            default_words = ["apple", "banana", "cherry", "date", "elderberry"]
            with open(self.dictionary_file, "w") as file:
                file.write("\n".join(default_words))
            return default_words

    def play_round(self):
        answer = random.choice(self.words).lower()
        guessed_letters = set()
        attempts_left = self.max_attempts

        print("\nNew Round!")
        while attempts_left > 0:
            print(self.HANGMAN_PICS[self.max_attempts - attempts_left])
            print("Word:", " ".join(letter if letter in guessed_letters else "_" for letter in answer))
            print("Guessed letters:", " ".join(sorted(guessed_letters)))
            print("Attempts left:", attempts_left)

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Enter a single alphabet.\n")
                continue
            if guess in guessed_letters:
                print("You already guessed that letter.\n")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                print(f"Good job! '{guess}' is in the word.\n")
            else:
                print(f"Sorry! '{guess}' is NOT in the word.\n")
                attempts_left -= 1

            if all(letter in guessed_letters for letter in answer):
                print(f"Congratulations! You guessed the word: {answer}")
                self.score["wins"] += 1
                return

        print(self.HANGMAN_PICS[-1])
        print(f"Game over! The word was: {answer}")
        self.score["losses"] += 1

    def play(self):
        print("Welcome to the Enhanced Word Guessing Game!\n")
        while True:
            self.play_round()
            print(f"Score => Wins: {self.score['wins']}, Losses: {self.score['losses']}\n")
            again = input("Do you want to play another round? (y/n): ").lower()
            if again != "y":
                print("Thanks for playing! Goodbye.")
                break

if __name__ == "__main__":
    game = WordGuessGame()
    game.play()
