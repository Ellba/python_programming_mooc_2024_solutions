# Write your solution here

string = input("Please type in a sentence: ")
x = string.split(' ')
while x != "":
    for i in x:
        print(i[0])
    break