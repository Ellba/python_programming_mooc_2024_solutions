# Write your solution here
def all_the_longest(l):
    new = []
    x = 0 
    for i in l:
        if len(i) > x:
            x = len(i)
    
    for i in l:
        if len(i) == x:
            new.append(i)
    
    return new


if __name__ == "__main__":
    print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))
    # all_the_longest()