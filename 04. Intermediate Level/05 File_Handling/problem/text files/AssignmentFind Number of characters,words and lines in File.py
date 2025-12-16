with open("data.txt", "r") as file:
    num_of_characters = 0
    num_of_words = 0
    num_of_lines = 0
    for line in file:
        num_of_lines += 1
        words = line.split()
        num_of_words += len(words)
        num_of_characters += len(line)
    print(num_of_characters, num_of_words, num_of_lines)