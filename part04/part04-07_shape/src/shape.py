# Copy here code of line function from previous exercise and use it in your solution
def line(num, string):
    if string == "":
        string = "*"
    print(int(num)*string[0])

def shape(width, character, height, fill):
    x = 1
    while width >= x: 
        line(x, character)
        x += 1
    
    while height > 0: 
        line(width, fill)
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # shape(5, "x")
    shape(5, "x", 2, "o")