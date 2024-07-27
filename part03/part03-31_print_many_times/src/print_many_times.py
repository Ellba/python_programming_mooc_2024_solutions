# Write your solution here
def print_many_times(text, num):
    while num > 0:
        print(text)
        num -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)