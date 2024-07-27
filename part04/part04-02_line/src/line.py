# Write your solution here
def line(num, string):
    if string == "":
        string = "*"
    print(int(num)*string[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")