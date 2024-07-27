# Write your solution here

# def simple_eval(expression):
#     allowed_chars = "0123456789+- "
#     if all(char in allowed_chars for char in expression):
#         return eval(expression)
#     else:
#         raise ValueError("Invalid characters in expression")


def filter_solutions():
    with open("solutions.csv") as file:
        new = []
        correct = [] 
        incorrect = []
        for line in file:
            new.append(line.strip().split(';'))

        # print(new)
        # for i in new:
        #     i[1] = eval(i[1])
        #     i[2] = int(i[2])

        for i in new:
            if eval(i[1]) == int(i[2]):
                correct.append(i)
            else:
                incorrect.append(i)
        # print('CORRECT',correct)
        # print('INCORRECT', incorrect)
    
    with open("correct.csv", "w") as correct_file:
        for x in correct:
            line = ""
            for value in x:
                line += f"{value};"
            line = line[:-1]
            correct_file.write(line+"\n")

    with open("incorrect.csv", "w") as incorrect_file:
        for x in incorrect:
            line = ""
            for value in x:
                line += f"{value};"
            line = line[:-1]
            incorrect_file.write(line+"\n")





if __name__ == "__main__":
    filter_solutions()