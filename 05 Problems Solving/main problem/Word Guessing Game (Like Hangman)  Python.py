import random


class WordGuessingGame:
    """
    A simple word guessing game similar to Hangman.
    """
    def __init__(self):
        """
        Initialize the game with a list of words and set up game state.
        
        Attributes:
            words (list): List of words to choose from.
            word (str): The word to be guessed.
            guessed (set): Set of letters that have been guessed.
            attempts (int): Number of attempts left.
        """
        self.words = ["apple", "banana", "cherry", "date", "elderberry"]
        self.word = random.choice(self.words)
        self.guessed = set()
        self.attempts = 6

    def display_word(self):
        """
        Display the current state of the word with guessed letters revealed.
        """
        display = ""

        for letter in self.word:

            if letter in self.guessed:
                display += letter + " "
            else:
                display += "_ "

        return display

    def play(self):
        """
        Main game loop.
        """

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