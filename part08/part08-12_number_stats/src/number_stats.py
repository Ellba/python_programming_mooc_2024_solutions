# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.sum = 0
        self.even_sum = 0
        self.odd_sum = 0

    def add_number(self, number:int):
        self.counter += 1
        self.sum += number
        if number % 2 == 0:
            self.even_sum += number
        else:
            self.odd_sum += number

    def count_numbers(self):
        return self.counter

    def get_sum(self):
        if self.counter == 0:
            self.sum = 0 
        return self.sum

    def average(self):
        if self.counter == 0:
            return 0
        return self.sum/self.counter

    def get_even_sum(self):
        return self.even_sum
    
    def get_odd_sum(self):
        return self.odd_sum


def main():
    stats = NumberStats()
    while True:
        user_num = int(input("Please type in integer numbers: "))
        if user_num == -1:
            break
        stats.add_number(user_num)        
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats.get_even_sum())
    print("Sum of odd numbers:", stats.get_odd_sum())

main()
