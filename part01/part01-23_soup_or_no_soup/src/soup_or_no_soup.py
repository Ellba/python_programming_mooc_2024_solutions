# Write your solution here

name = input("Please tell me your name: ")
if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    cost = 5.9 * portions
    print("The total cost is", cost)
print("Next please!")