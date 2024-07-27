# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        string = "*"
    print(int(num)*string[0])

def triangle(size):
    # You should call function line here with proper parameters
    x = 1
    while size >= x: 
        line(x, "#")
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
