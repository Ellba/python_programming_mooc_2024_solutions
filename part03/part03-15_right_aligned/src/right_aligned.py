# Write your solution here
string = input("Please type in a string: ")
stars = (20 - len(string)) * "*" + string
print(stars)