# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int): 
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)


    # end_column = column_no + 3
    # block = []
    # for i in range(0, 3): 
    #     new_row = sudoku[row_no+i][column_no:end_column]
    #     print(new_row)
    #     block.append(new_row)
    #     i += 1
    
    # flat = [item for row in block for item in row]
    # numbers = []

    # for number in flat:
    #     if number > 0 and number in numbers:
    #         return False
    #     numbers.append(number)
 
    return True



if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 1, 2))
    # print(block_correct(sudoku, 1, 2))