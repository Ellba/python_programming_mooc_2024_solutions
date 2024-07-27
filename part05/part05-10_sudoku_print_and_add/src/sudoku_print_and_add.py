# Write your solution here



def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()


    # text = sudoku[:]
    # for row in range(9):
    #     for i in range(9):
    #         if text[row][i] == 0:
    #             text[row][i] = '_'
    #         else:
    #             text[row][i] = str(text[row][i])
    
    # for row in text:
    #     for i in range(9):
    #         if i in (2,5):
    #             row[i] += '  '
    #         elif i == 9:
    #             row[i] += '\n\n'
    #         else:
    #             row[i] += ' '

    # for row in range(9):
    #     line = ''.join(text[row])
    #     if row == 2 or row == 5:
    #         print(line+'\n') 
    #     else:
    #         print(line)
        

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":
    sudoku  = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 5, 2)