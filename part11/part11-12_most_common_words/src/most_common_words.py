# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as f:
        words = [i.replace(".","").replace(",","") for i in f.read().strip().split()]
        return {i: words.count(i) for i in words if words.count(i) >= lower_limit} 

if __name__ == "__main__":
    print(most_common_words("programming.txt", 3))