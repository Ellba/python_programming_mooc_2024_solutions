# Write your solution here:

class Item:
    def __init__(self, name_input, weight_input):
        self.name_input = name_input
        self.weight_input = weight_input

    def name(self):
        return self.name_input

    def weight(self):
        return self.weight_input

    def __str__(self):
        return f"{self.name_input} ({self.weight_input} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcase_items = []

    def add_item(self, item):
        if item.weight() <= self.max_weight:
            self.suitcase_items.append(item)
            self.max_weight -= item.weight()

    def print_items(self):
        for i in self.suitcase_items:
            print(i)

    def weight(self):
        return sum(i.weight() for i in self.suitcase_items)

    def heaviest_item(self):
        heavy = self.suitcase_items[0]
        for i in self.suitcase_items:
            if i.weight() > heavy.weight():
                heavy = i
        return heavy


    def __str__(self):
        return f"{len(self.suitcase_items)} {'item' if len(self.suitcase_items) == 1 else 'items'} ({self.weight()} kg)" 


class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []
    
    def add_suitcase(self, suitcase):
        if suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)
            self.max_weight -= suitcase.weight()

    def print_items(self):
        for cargo in self.suitcases:
            cargo.print_items()

    def __str__(self):
        return f"{len(self.suitcases)} {'suitcase' if len(self.suitcases) == 1 else 'suitcases'}, space for {self.max_weight} kg"


if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    print(suitcase)