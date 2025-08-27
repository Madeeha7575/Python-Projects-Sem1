#Palindrome Checker

def palindrome(word):
    word = word.lower().replace(" ","")
    reversed_word = word[::-1]
    return word == reversed_word
user_word = input("Enter a word:")
if palindrome(user_word):
    print("Its a palindrome.")
else:
    print("it is not a palindrome")
    
