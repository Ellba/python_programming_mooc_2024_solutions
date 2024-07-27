# Write your solution here:

class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"FINISHED" if self.finished is True else "NOT FINISHED"}"


    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True



class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.__orders.append(order)

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return list(set([i.programmer for i in self.__orders]))

    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return 
        raise ValueError("id not found")

    def finished_orders(self):
        return [order for order in self.__orders if order.is_finished() is True]

    def unfinished_orders(self):
        return [order for order in self.__orders if order.is_finished() is False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("programmer not found")
        finished = [i for i in self.finished_orders() if i.programmer == programmer]
        unfinished = [i for i in self.unfinished_orders() if i.programmer == programmer]
        sum_workload_fin = sum(i.workload for i in finished)
        sum_workload_unfin = sum(i.workload for i in unfinished)
        return (len(finished), len(unfinished), sum_workload_fin, sum_workload_unfin)
                




if __name__ == "__main__":
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.add_order("program mobile app", "Andy", 5)
    t.add_order("program something with pygame", "Andy", 50)
    t.add_order("code better facebook", "Jonas", 5000)
    x = [i for i in t.all_orders()]
    for i in x:
        print(i)
    # print([(i.description, i.programmer) for i in t.finished_orders() if i.programmer == "Andy"])
    # print([(i.description, i.programmer) for i in t.unfinished_orders() if i.programmer == "Andy"])
    # print([(i.id, i.is_finished()) for i in t.all_orders()])
    # t.mark_finished(1)
    # print([(i.description, i.programmer) for i in t.finished_orders() if i.programmer == "Andy"])
    # print([(i.description, i.programmer) for i in t.unfinished_orders() if i.programmer == "Andy"])
    # print([(i.id, i.is_finished()) for i in t.all_orders()])
    # t.mark_finished(2)
    # print([(i.description, i.programmer) for i in t.finished_orders() if i.programmer == "Andy"])
    # print([(i.description, i.programmer) for i in t.unfinished_orders() if i.programmer == "Andy"])
    # print([(i.id, i.is_finished()) for i in t.all_orders()])
    # print(t.status_of_programmer("Andy"))
    # expected return is (2, 1, 15, 50)