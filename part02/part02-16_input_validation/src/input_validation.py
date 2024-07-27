from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number > 0:
        print(sqrt(number))
    else:
        print("Invalid number")
        
print("Exiting...")