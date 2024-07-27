# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    selection = int(input("Function: "))
    if selection == 3: 
        print("Bye now!")
        break 
    elif selection == 1:
        fi = input("The word in Finnish: ")
        en = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{fi} - {en}\n")
        print("Dictionary entry added")
    elif selection == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                print(line.replace('\n', ''))