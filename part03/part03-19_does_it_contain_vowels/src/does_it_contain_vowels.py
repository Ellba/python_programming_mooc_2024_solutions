# Write your solution here
string = input("Please type in a string: ")
vowels = ["a", "e", "o"]
for i in vowels:
    if i in string:
        print(f"{i} found")
    else:
        print(f"{i} not found")

"""
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
"""