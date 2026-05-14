import random


class WordGuessingGame:

    def __init__(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry"]
        self.word = random.choice(self.words)
        self.guessed = set()
        self.attempts = 6

    def display_word(self):

        display = ""

        for letter in self.word:

            if letter in self.guessed:
                display += letter + " "
            else:
                display += "_ "

        return display

    def play(self):

        while self.attempts > 0:

            print("\nWord:", self.display_word())
            print("Attempts left:", self.attempts)
            print("Guessed letters:", self.guessed)

            guess = input("Guess a letter: ").lower()

            # validation
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter only one letter!")
                continue

            # already guessed
            if guess in self.guessed:
                print("You already guessed this letter!")
                continue

            # correct guess
            if guess in self.word:
                print("Correct!")
                self.guessed.add(guess)

            else:
                print("Wrong!")
                self.attempts -= 1

            # win check
            won = True

            for letter in self.word:

                if letter not in self.guessed:
                    won = False

            if won:
                print("\nCongratulations! You guessed the word:", self.word)
                return

        print("\nGame Over! The word was:", self.word)


if __name__ == "__main__":

    game = WordGuessingGame()
    game.play()