# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    fraction = Fraction(1, amount)
    return [fraction] * amount


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))