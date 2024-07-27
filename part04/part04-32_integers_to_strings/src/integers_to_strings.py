# Write your solution here
def formatted(l1):
    new = []
    for i in l1:
        x = f"{i:.2f}"
        new.append(x)
    return new


if __name__ == "__main__":
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))