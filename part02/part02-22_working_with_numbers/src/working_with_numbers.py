# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")
numbers_list = []
while True:
    n = int(input("Number: "))
    numbers_list.append(n)
    if n == 0:
        numbers_list.pop(-1)
        break
l = len(numbers_list)
s = sum(numbers_list)
m = s/l
negative = len(list(filter(lambda x: (x < 0), numbers_list)))
positive = len(list(filter(lambda x: (x >= 0), numbers_list)))

print(f"Numbers typed in {l}")
print(f"The sum of the numbers is {s}")
print(f"The mean of the numbers is {m}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

"""
numbers = 0
sum = 0
positives = 0
 
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    sum += number
    if number>0:
        positives += 1
 
print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)
"""