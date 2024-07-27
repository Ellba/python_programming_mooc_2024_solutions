# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __to_float(self) -> float:
        return (self.__euros + self.__cents /100)

    def __eq__(self, another):
        return self.__to_float() == another.__to_float()

    def __gt__(self, another):
        return self.__to_float() > another.__to_float()

    def __lt__(self, another):
        return self.__to_float() < another.__to_float()

    def __ne__(self, another):
        return self.__to_float() != another.__to_float()

    def __add__(self, another):
        total_cents = self.__cents + another.__cents
        new_euros = self.__euros + another.__euros + total_cents // 100
        new_cents = total_cents % 100
        return Money(new_euros, new_cents)

    def __sub__(self, another):
        total_cents_self = self.__euros * 100 + self.__cents
        total_cents_another = another.__euros * 100 + another.__cents
        result_cents = total_cents_self - total_cents_another
        
        if result_cents < 0:
            raise ValueError("a negative result is not allowed")
        
        new_euros = result_cents // 100
        new_cents = result_cents % 100
        return Money(new_euros, new_cents)

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    e4 = e1 + e2
    # e5 = e1 - e2

    print(e4)
    # print(e5)

    print(e1)
    e1.euros = 1000
    print(e1)

    # e6 = e2-e1

    money1 = Money(2, 50)
    money2 = Money(2, 50)
    print(money1 + money2)