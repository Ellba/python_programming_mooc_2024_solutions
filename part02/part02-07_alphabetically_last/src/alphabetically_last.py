# Write your solution here
w1 = input("Please type in the 1st word: ").lower()
w2 = input("Please type in the 2nd word: ").lower()
if w1 > w2:
    print(f"{w1} comes alphabetically last.")
elif w1 < w2:
    print(f"{w2} comes alphabetically last.")
elif w1 == w2:
    print(f"You gave the same word twice.")