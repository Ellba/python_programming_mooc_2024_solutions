# Write your solution here

def even_numbers(list):
    new = []
    for i in list:
        if i % 2 == 0:
            new.append(i)
    return new

if __name__ == "__main__":
    even_numbers()