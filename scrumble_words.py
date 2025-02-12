import random

def scramble_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
        return word

word = input("Enter a word: ")
print("Scrambled word:", scramble_word(word))