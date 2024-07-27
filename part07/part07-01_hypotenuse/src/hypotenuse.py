# Write your solution here
from math import sqrt, hypot

def hypotenuse(leg1: float, leg2: float):
    return hypot(leg1, leg2)

if __name__ == "__main__":
    print(hypotenuse(3,4))