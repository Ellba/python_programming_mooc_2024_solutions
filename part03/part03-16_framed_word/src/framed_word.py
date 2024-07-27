# Write your solution here
string = input("Please type in a string: ")
row = "*" * 30
start = "\n*"
c = int(14 - len(string)/2)
space = " " * c + string
end = " " * (28 - len(space))

s1 = row + start + space + end + "*" + "\n" + row

print(s1)

"""
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)
"""