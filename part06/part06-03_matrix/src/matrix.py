# write your solution here


def matrix_sum():
    return sum(row_sums())

def matrix_max():
    matrix = convert()
    biggest = 0
    for i in matrix:
        if max(i) > biggest:
            biggest = max(i)
    return biggest


def row_sums():
    matrix = convert()
    sum_list = []
    for i in matrix:
        sum_list.append(sum(i))

    return sum_list
            
def convert():
    with open("matrix.txt") as matrix:
        new_matrix = []
        for line in matrix:
            line = line.replace('\n', '') 
            lst = line.split(',')
            lst = [int(i) for i in lst]
            new_matrix.append(lst)
    return new_matrix

if __name__ == "__main__":
    matrix_sum()
    row_sums()
    matrix_max()