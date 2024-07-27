# Write your solution here
from random import randint, sample

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = list(range(lower, upper))
    pick = sorted(sample(numbers, amount))
    return pick

if __name__ == "__main__":
    lottery_numbers(7, 1, 40)
    # for number in lottery_numbers(7, 1, 40):
    #     print(number)