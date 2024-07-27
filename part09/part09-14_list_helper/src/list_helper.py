# WRITE YOUR SOLUTION HERE:
from collections import Counter
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        return max(set(my_list), key = my_list.count)

    @classmethod
    def doubles(cls, my_list: list):
        item_counts = Counter(my_list)
        return sum(1 for count in item_counts.values() if count >= 2)


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))