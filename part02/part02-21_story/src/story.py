# Write your solution here
words = []
while True:
    word = input("Please type in a word: ")
    words.append(word)
    if len(words) > 1:
        if word == "end" or word == words[-2]:
            break
print(' '.join(words[:-1]))