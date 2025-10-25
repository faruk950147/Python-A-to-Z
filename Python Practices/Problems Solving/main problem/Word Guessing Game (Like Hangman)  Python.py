import random
import os

def load_dictionary(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        return words
    else:
       with open(file_path, "w") as file:
           file.write("apple\nbanana\ncherry\ndate\nelderberry")
           return ["apple", "banana", "cherry", "date", "elderberry"]

def is_valid_guess(guess, guessed_letters):
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters

def display_word(answer, guessed_letters):
    displayed = ""
    for letter in answer:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def play(words, answer):
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to the Word Guessing Game!")
    print("You have", attempts, "attempts to guess the letters in the word.")

    while attempts > 0:
        print("\nWord:", display_word(answer, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        if not is_valid_guess(guess, guessed_letters):
            print("Invalid guess or already guessed. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry! '{guess}' is NOT in the word.")
            attempts -= 1
        
        # Check if all letters are guessed
        if all(letter in guessed_letters for letter in answer):
            print("\nCongratulations! You guessed the word:", answer)
            return
    
    print("\nGame over! The word was:", answer)

# Load words and start game
words = load_dictionary("dictionary.txt")
if words:
    answer = random.choice(words).lower()
    play(words, answer)


# def word_choosing(word_list):
#     return random.choice(word_list).lower()

# def word_status(word, guessed_letters):
#     display_word = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display_word += letter + " "
#         else:
#             display_word += "_ "
#     return display_word.strip()

# def word_guessing_game():
#     secret_word = word_choosing(["apple", "banana", "cherry", "date", "elderberry"])
#     guessed_letters = []
#     attempts = 6

#     print("\n" + "Welcome to the Word Guessing Game!".center(60))
#     print(("The word has " + str(len(secret_word)) + " letters.").center(60))
#     print("\nSecret Word:", word_status(secret_word, guessed_letters))
#     print("Attempts left:", attempts)

#     while attempts > 0:
#         guess = input("\nGuess a letter: ").lower()

#         # input validation
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue
#         if guess in guessed_letters:
#             print("You already guessed that letter:", guess)
#             continue

#         guessed_letters.append(guess)

#         # correct/wrong
#         if guess in secret_word:
#             print("Correct!")
#         else:
#             attempts -= 1
#             print("Wrong! Attempts left:", attempts)

#         # current status
#         current_status = word_status(secret_word, guessed_letters)
#         print("Secret Word:", current_status)
#         print("Guessed Letters:", " ".join(guessed_letters))

#         # check if the word is guessed
#         if "_" not in current_status:
#             print("\nCongratulations! You guessed the word:", secret_word)
#             return

#     # all attempts are over
#     print("\nGame Over! The word was:", secret_word)

# word_guessing_game()



# ==================== efficient code ====================

# def word_guessing_game():
#     words = ["apple", "banana", "cherry", "date", "elderberry"]
#     word = random.choice(words)
#     guessed = set()
#     attempts = 6

#     print("Welcome to the Word Guessing Game!".center(50))
#     print("The word has " + str(len(word)) + " letters.".center(50))

#     while attempts > 0:
#         display = ''.join([letter if letter in guessed else '_' for letter in word])
#         print("\nWord:", display)

#         if '_' not in display:
#             print("\nYou guessed it! The word was '{word}'.")
#             return

#         guess = input("Guess a letter: ").lower()

#         if not (len(guess) == 1 and guess.isalpha()):
#             print("Enter a single valid letter.")
#             continue
#         if guess in guessed:
#             print("You already guessed that letter.")
#             continue

#         guessed.add(guess)
#         if guess in word:
#             print("Correct!")
#         else:
#             attempts -= 1
#             print("Wrong! Attempts left: {attempts}")

#     print("Game over! The word was '{word}'.")
