# Write your solution here
import random

def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]

def play(dice1: str, dice2: str, times: int):
    result = [0, 0, 0]
    for i in range(times):
        one = roll(dice1)
        two = roll(dice2)
        if one > two:
            result[0] += 1
        elif one < two:
            result[1] += 1
        elif one == two:
            result[2] += 1 

    return tuple(result)

if __name__ == "__main__":
    result = play("A", "B", 100)
    print(result)
    # result = play("B", "B", 1000)
    # print(result)