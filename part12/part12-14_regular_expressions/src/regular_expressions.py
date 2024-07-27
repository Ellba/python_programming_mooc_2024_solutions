# Write your solution here
import re

def is_dotw(my_string: str):
    pattern = r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b'
    return bool(re.search(pattern, my_string))

def all_vowels(my_string: str):
    return bool(re.search("^[aeiou]+$", my_string))

def time_of_day(my_string: str):
    return bool(re.search("^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string))


if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("25:13:01"))