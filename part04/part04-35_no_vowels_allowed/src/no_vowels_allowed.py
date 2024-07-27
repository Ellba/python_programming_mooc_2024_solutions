# Write your solution here
def no_vowels(string):
    v = ["i", "a", "e", "o", "u"]
    for i in v:
        string = string.lower().replace(i,"")
    # string = string.lower().replace("i", "").replace("a","").replace("e","").replace("o","").replace("u","")
    return string

if __name__ == "__main__":
    # most_common_character()
    print(no_vowels("this is an example"))