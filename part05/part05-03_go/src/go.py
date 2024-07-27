# Write your solution here

def who_won(game_board: list):
    p1 = p2 = 0
    for row in game_board:
        for num in row:
            if num == 1:
                p1 += 1
            if num == 2:
                p2 += 1
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else: 
        return 0



if __name__ == "__main__":
    # who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]])
    print(who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]]))