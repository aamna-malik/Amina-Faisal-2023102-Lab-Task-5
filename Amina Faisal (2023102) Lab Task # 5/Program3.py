word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if len(word1) != len(word2):
    print("The words are not anagrams.")
else:
    if sorted(word1) == sorted(word2):
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")