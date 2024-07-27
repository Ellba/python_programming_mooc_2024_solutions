# write your solution here

def read_fruits():
    fruitdict = {}
    with open("fruits.csv") as fruits:
        #print(fruits.read())
        for line in fruits:
            parts = line.split(";")
            #print('line',line, 'parts',parts)
            fruitdict[parts[0]] = float(parts[1])
    print(fruitdict)
    return fruitdict

if __name__ == "__main__":
    read_fruits()