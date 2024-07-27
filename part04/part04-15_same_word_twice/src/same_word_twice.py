# Write your solution here
l = []
while True:
    word = input("Word: ")
    if word in l:
        break
    l.append(word)
    # l.append(word)
    # if l.count(word) > 1:
    #     break
print(f"You typed in {len(l)} different words")
# print(f"You typed in {len(set(l))} different words")
