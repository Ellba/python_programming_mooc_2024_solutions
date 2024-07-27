# Write your solution here
def sudoku_grid_correct(sudoku):
    print(sudoku)
  
    hset = set()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] > 0 and sudoku[i][j] in hset:
                return False
            hset.add(sudoku[i][j])
        hset = set()


    for i in range(9):
        for j in range(9):
            # print(sudoku[j][i], hset)
            if sudoku[j][i] > 0 and sudoku[j][i] in hset:
                return False
            hset.add(sudoku[j][i])
        hset = set()


    blocks = []
    for row in (0, 3, 6):
        for col in (0, 3, 6):
            block = [sudoku[i][j] for i in range(row, row+3) for j in range(col, col+3)]
            blocks.append(block)

    for line in blocks:
        for num in line:
            if num > 0 and num in hset:
                return False
            hset.add(num)
        hset = set()
    
    return True
    
"""
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
 
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True
 
def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True

"""



if __name__ == "__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 1, 6, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

   
    print(sudoku_grid_correct(sudoku))
    