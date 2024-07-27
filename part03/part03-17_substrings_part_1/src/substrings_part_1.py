# Write your solution here
string = input("Please type in a string: ")
n = 1
while n <= len(string):
    print(string[:n])
    n += 1