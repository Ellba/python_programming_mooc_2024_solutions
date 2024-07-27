# Write your solution here

def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

if __name__ == "__main__":
    matrix = [[10, 100], [10, 100]]
    print(transpose(matrix))

    # [[10, 100], [10, 100]] != [[10, 10], [100, 100]]