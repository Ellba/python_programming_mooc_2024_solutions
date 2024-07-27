# Write your solution here

print("1 - add an entry, 2 - read entries, 0 - quit")

while True:
    selection = int(input("Function: "))
    if selection == 0: 
        print("Bye now!")
        break 
    elif selection == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry+'\n')
        print("Diary saved")
    elif selection == 2:
        print("Entries:")
        with open("diary.txt") as file:
            print(file.read())