# Write your solution here

while True: 
    editor = input("Editor: ").lower()
    if editor == "visual studio code":
        break
    if editor == "notepad" or editor == "word":
        print("awful")
    else:
        print("not good")
            
print("an excellent choice!")