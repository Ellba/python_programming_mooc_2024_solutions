# Write your solution here
import math

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break
    
    print(f"The factorial of the number {num} is {math.factorial(num)}")
print("Thanks and bye!")