def count_char(ch, text):
    total = 0
    for c in range(len(text)):
        if text[c] == ch:
            total += 1
    return total
