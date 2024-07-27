class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list):
    return sorted(routes, key=lambda route: route.length, reverse=True)


def sort_by_difficulty(routes: list):
    return sorted(routes, key=lambda route: (route.grade[0], route.grade[1:], route.length), reverse=True)



if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 9, "7A")
    r3 = ClimbingRoute("Syncro", 14, "8C+")
    reply = sort_by_difficulty([r1, r2, r3])

    for i in reply:
        print(i)
