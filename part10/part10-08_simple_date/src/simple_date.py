# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __convert_days(self):
        return self.day + self.month * 30 + self.year * 360

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, another):
        return True if self.__convert_days() == another.__convert_days() else False

    def __gt__(self, another):
        return True if self.__convert_days() > another.__convert_days() else False

    def __lt__(self, another):
        return True if self.__convert_days() < another.__convert_days() else False

    def __add__(self, days):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        
        return SimpleDate(new_day, new_month, new_year)

    
    def __sub__(self, another):
        return abs(self.__convert_days() - another.__convert_days())


    # 4.10.2020 < 28.12.1985

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2==d1)
    # print(d1-d2)
    # print(d1-d3)