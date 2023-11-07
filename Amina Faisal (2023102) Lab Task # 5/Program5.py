word = input("Enter a word: ")

vowels = 0
consonants = 0

for char in word:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print(f"The word '{word}' has {vowels} vowels and {consonants} consonants.")