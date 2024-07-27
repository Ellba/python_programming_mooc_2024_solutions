# Write your solution here
def length_of_longest(names: list):
    longest = 0
 
    for name in names:
        if len(name) > longest:
          longest = len(name)
 
    return longest


    # new = []
    # for i in list:        
    #     new.append(len(i))       

    # return max(new)

if __name__ == "__main__":
    #print(length_of_longest(["first", "second", "fourth", "eleventh"]))
    length_of_longest()