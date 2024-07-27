# Write your solution here
my_list = []

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "x":
        break
    if choice == "d":
        item = len(my_list) + 1
        my_list.append(item)
    if choice == "r":
        my_list.pop(len(my_list)-1)
        
print("Bye!")
