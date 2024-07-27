# Write your solution here

def sum_of_positives(list: list):
    x = 0
    for i in list:
        if i > 0:
            x += i
    return x

# print(sum_of_positives(my_list))

if __name__ == "__main__":
    sum_of_positives()