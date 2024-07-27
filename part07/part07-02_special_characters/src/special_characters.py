# Write your solution here
import string

def separate_characters(my_string: str):
    result = ["","",""]
    for i in my_string:
        if i in string.ascii_letters:
            result[0] += i
        elif i in string.punctuation:
            result[1] += i
        else:
            result[2] += i
    return tuple(result)



if __name__ == "__main__":
    # separate_characters("Olé!!! Hey, are ümläüts wörking?")
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts)
    print(parts[0])
    print(parts[1])
    print(parts[2])