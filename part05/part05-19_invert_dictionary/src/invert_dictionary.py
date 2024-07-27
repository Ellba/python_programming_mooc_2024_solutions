# Write your solution here

def invert(dictionary: dict):
    # next = {v: k for k, v in dictionary.items()}
    # print(next)

    temp = {}

    for key, value in dictionary.items():
        temp[value] = key

    dictionary.clear()

    for key, value in temp.items():
        dictionary[key] = value

if __name__ == "__main__":
    # s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    s = {1: 10, 2: 20, 3: 30}
    invert({1: 10, 2: 20, 3: 30})