# Write your solution here
# If you use the classes made in the previous exercise, copy them here


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
        sum_workload_fin = sum(int(i.workload) for i in finished)
        sum_workload_unfin = sum(int(i.workload) for i in unfinished)
        return (len(finished), len(unfinished), sum_workload_fin, sum_workload_unfin)
                

class OrderBookApplication:
    def __init__(self):
        self.__order_book = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self): 
        description = input("description: ")
        programmer_workload = input("programmer and workload estimate: ")
        
        try: 
            programmer = programmer_workload.split()[0]
            workload = programmer_workload.split()[1]
            int(workload)
        except ValueError:
            print("erroneous input")   
            return
        except IndexError:
            print("erroneous input")   
            return
        self.__order_book.add_order(description, programmer, workload)
        print("added!")

    def list_finished_tasks(self):
        finished = [i for i in self.__order_book.finished_orders()]
        if finished != []:
            for i in finished:
                print(i)
        else:
            print("no finished tasks")

    
    def list_unfinished_tasks(self):
        unfinished = [i for i in self.__order_book.unfinished_orders()]
        if unfinished == []:
            print("no unfinished tasks")
            return
        for i in unfinished:
            print(i)
        

    def mark_task_as_finished(self):
        try:
            id = int(input("id: "))
            self.__order_book.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def get_programmers(self):
        programmers = self.__order_book.programmers()
        if programmers:
            for i in programmers:
                print(i)
        print("erroneous input")


    def programmer_status(self):
        programmer = input("programmer: ")
        try:
            r = self.__order_book.status_of_programmer(programmer)
            print(f"tasks: finished {r[0]} not finished {r[1]}, hours: done {r[2]} scheduled {r[3]}")
        except ValueError:
            print("erroneous input")
    

        
    def execute(self):
        self.help()
        while True: 
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_task_as_finished()
            elif command == "5":
                self.get_programmers()
            elif command == "6":
                self.programmer_status()
            else:
                print("Invalid request, stopping application...")
                break







application = OrderBookApplication()
application.execute()