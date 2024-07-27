# Write your solution here
l = []
num = int(input("How many items: "))

while len(l) < num:
    item = int(input(f"Item {len(l) + 1}: "))
    l.append(item)

print(l)