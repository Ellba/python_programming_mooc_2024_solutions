# Write your solution here

num = int(input("Please type in a number "))

x = 1
while x <= num:
    y = 1
    while y <= num:
        print(f"{x} x {y} = {x*y}")
        y += 1
    x += 1


"""
i = 1

while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1
"""