# Write your solution here
def no_shouting(l1):
    new = []
    for i in l1:
        if not i.isupper():
            new.append(i)

    return new


if __name__ == "__main__":
    no_shouting()
    # print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))