# Write your solution here
import string
def change_case(orig_string: str):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in orig_string])

def split_in_half(orig_string: str):
    return orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]

def remove_special_characters(orig_string: str):
    allow = string.ascii_letters + string.digits + ' '
    return ''.join([i for i in orig_string if i in allow])

if __name__ == "__main__":
    # change_case("This is a test, lets see how it goes!!!11!")
    print(remove_special_characters("This is a test, lets see how it goes!!!11!"))