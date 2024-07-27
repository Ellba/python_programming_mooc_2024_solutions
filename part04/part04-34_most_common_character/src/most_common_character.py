# Write your solution here
def most_common_character(string: str):
    x = string[0]
    for i in string:
        if string.count(i) > string.count(x):
            x = i
        
    return x

if __name__ == "__main__":
    most_common_character()