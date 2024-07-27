# Write your solution here
l = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(l):
        print("Index is outside of the range of the list")
        continue
    new_value = int(input("New value: "))
    l[index] = new_value
    print(l)
