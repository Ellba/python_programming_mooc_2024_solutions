# Write your solution here
p = input("Password: ")
while True:
    r = input("Repeat password: ")
    if p == r:
        break
    print("They do not match!")

print("User account created!")