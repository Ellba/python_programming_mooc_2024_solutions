# Write your solution here
def same_chars(str, a, b):
    # try:
    #     if string[index1] == string[index2]:
    #         return True
    #     else:
    #         return False
    # except IndexError:
    #     return False

    if a >= len(str) or b >= len(str):
        return False
    return str[a] == str[b]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
    print(same_chars("programmer", 0, 4))
    same_chars("coder", 1, 10)