# Write your solution here
p = int(input("Please type in a positive integer: "))
for i in range(-p, p+1):
    # Because in Python bool-type equals to
    # 0 and 1 (False and True), condition can also be written as follows
    # if i:
    if i != 0:
        print(i)