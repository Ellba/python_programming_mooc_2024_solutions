# write your solution here


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

names = {}
with open(student_info) as students:
    for line in students:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = f"{parts[1]} {parts[2].strip()}"

exercises = {}
with open(exercise_data) as ex:
    for line in ex:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        parts[1:] = [int(i.strip()) for i in parts[1:]]
        exercises[parts[0]] = parts[1:]

for id, name in names.items():
    if id in exercises:
        sum_ex = sum(exercises[id])
        print(name, sum_ex)