# Write your solution here
def chessboard(length):
    tokens = ["0", "1"]
    for x in range(length):
        for y in range(length):
            i = tokens[(x + y + 1) % 2]
            print(i, end=(''))
        print()


# i = 0
#     while i < size:
#         if i % 2 == 0:
#             row = "10"*size
#         else:
#             row = "01"*size
#         # Remove extra characters at the end of the row
#         print(row[0:size])
#         i += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
