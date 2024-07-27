# Write your solution here
def everything_reversed(l1):
    new = []
    for i in l1[::-1]:
        new.append(i[::-1])
    return new

if __name__ == "__main__":
    print(everything_reversed(["Hi", "there", "example", "one more"]))