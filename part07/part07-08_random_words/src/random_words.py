# Write your solution here
from random import sample

def words(n: int, beginning: str):
    with open("words.txt") as file:
        wordlist = file.read().split('\n')
        pool = []
        for i in wordlist:
            if i.startswith(beginning) == True: 
                pool.append(i)

        if len(pool) < n:
            raise ValueError("Not enough suitable words can be found!")
        return sample(pool, n)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)