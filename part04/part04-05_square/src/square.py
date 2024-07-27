# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        string = "*"
    print(int(num)*string[0])

def square(size, character):
    # You should call function line here with proper parameters
    x = 0 
    while x < size:
        line(size, character)
        x += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")