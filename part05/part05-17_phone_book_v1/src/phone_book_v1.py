# Write your solution here
def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
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
    print(persons)
    print("quitting...")
 
main()


# book = {}
# while True:
#     request = input("command (1 search, 2 add, 3 quit): ")
#     if request == "3":
#         break
#     elif request == "2":
#         name_input = input("name: ")
#         number_input = input("number: ")
#         if name_input not in book:
#             book[name_input] = []
#             book[name_input].append(number_input)
#         else:
#             book[name_input][0] = number_input
#         print("ok!")
#     elif request == "1":
#         name_input = input("name: ")
#         if name_input not in book:
#             print("no number")
#         else:
#             print(book[name_input][0])

# print("quitting...")