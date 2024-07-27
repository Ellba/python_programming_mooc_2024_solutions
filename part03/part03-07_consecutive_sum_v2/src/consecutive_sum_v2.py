# Write your solution here
limit = int(input("Limit: "))
number = 1
sum = 1
l = ["1"]
while sum < limit:   
    number += 1
    sum += number
    l.append(str(number))
print("The consecutive sum:",' + '.join(l),'=',sum)


"""
limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")
"""