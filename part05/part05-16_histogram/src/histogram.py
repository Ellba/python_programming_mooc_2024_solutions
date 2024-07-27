# Write your solution here

def histogram(string: str):
    letters = {}
    for l in string:
        if l not in letters:
            letters[l] = 0
        letters[l] += 1
    
    for key, value in letters.items():
        print(f"{key} {value*'*'}")
    return letters

if __name__ == "__main__":
    histogram("statistically")