# Write your solution here
def spruce(num):
    print("a spruce!")
    for i in range(num):
        spaces = ' ' * (num - i - 1)
        branches = '*' * (2 * i + 1)
        print(spaces + branches)

    print(' ' * (num - 1) + '*')


    # n_branch = 1
    # n_space = num-1
    # i = 0
    # branch = "*" 
    # space = " "
    # print("a spruce!")
    # while i < num:     
    #     print(space * n_space + branch * n_branch)
    #     i += 1
    #     n_space -= 1
    #     n_branch += 2
    # print(space * (num-1) + branch)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)


#    *
#   ***
#  *****
# *******
#*********