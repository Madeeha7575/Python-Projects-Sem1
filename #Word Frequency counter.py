#Word Frequency counter
text = input("Enter a sentence:")
words = text.lower().split()
for word in set(words):
    print(word,"appears",words.count(word),"times.")


