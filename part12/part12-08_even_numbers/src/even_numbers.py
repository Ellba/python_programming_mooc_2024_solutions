# Write your solution here

def even_numbers(beginning: int, maximum: int):
    for i in range(beginning, maximum+1):
        if i % 2 == 0:
            yield i
            i += 2


if __name__ == "__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)