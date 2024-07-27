# Write your solution here

def read_input(text: str, value1: int, value2: int):
    while True:
        try:
            input_str = int(input(text))
            if input_str >= value1 and input_str <= value2:
                return input_str
        except ValueError:
            pass
         
        print(f"You must type in an integer between {value1} and {value2}")



if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)