# Write your solution here
from random import choice, sample
import string

def generate_password(num: int):
    letters = string.ascii_lowercase
    password = ''.join(sample(letters, num))
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))