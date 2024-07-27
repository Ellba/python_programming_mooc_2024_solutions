# write your solution here

def largest():
    l = []
    with open("./numbers.txt") as numbers:
        for n in numbers:
            n = n.replace("\n", "")
            l.append(int(n))            
    return max(l)

if __name__ == "__main__":
    largest()