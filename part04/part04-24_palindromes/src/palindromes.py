# Write your solution here
def palindromes(string: str):
    return string == string[::-1]
    
def main():
    while True:
        p = input("Please type in a palindrome: ")
        if palindromes(p):
            break
        print("that wasn't a palindrome")
            
    print(f"{p} is a palindrome!")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
#     main()
# block!
x = main()
# print(x)