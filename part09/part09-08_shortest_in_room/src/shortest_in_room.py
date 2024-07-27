# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.room_list = []

    def add(self, person: Person): 
        self.room_list.append(person)

    def is_empty(self):
        return len(self.room_list) == 0

    def shortest(self):
        if self.room_list != []:
            shortest_height = int(self.room_list[0].height)
            shortest_person = self.room_list[0]
            for i in self.room_list:
                if i.height < shortest_height:
                    shortest_height = i.height
                    shortest_person = i
            return shortest_person
        return None
                

    def remove_shortest(self):    
        shortest_person = self.shortest()
        if shortest_person:
            self.room_list.remove(shortest_person)
 
        return shortest_person

    def print_contents(self):
        print(f"There are {len(self.room_list)} persons in the room, and their combined height is {sum(i.height for i in self.room_list)} cm")
        for person in self.room_list:
            print(f"{person.name} ({person.height} cm)")

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()