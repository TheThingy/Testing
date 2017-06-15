word = str(input("Enter word: "))
if word == word[::-1]:
    print("The word is a palindrome")
else:
    print("the word is not a palindrome")