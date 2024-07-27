# Write your solution here

def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        row = person[0] + ";"
        row += str(person[1]) + ";"
        row += str(person[2])
 
        file.write(row + "\n")
   


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))