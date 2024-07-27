# Write your solution here
def search(persons):
    name = input("name: ")
    if name in persons:
        for i in persons[name]:
            print(i)
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()

# 2
# mary
# 040-234567
# 2
# mary
# 09-334455
# 1
# mary
# 3