# Write your solution here
def squared(string, num):
    x = string * num**2 
    y = 0
    while num > y:
        print(x[:num])
        x = x[num:]
        y += 1
        

if __name__ == "__main__":
    squared("ab", 3)