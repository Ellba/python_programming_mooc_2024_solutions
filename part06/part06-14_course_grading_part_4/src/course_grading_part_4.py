
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")
# student_info = "students1.csv"
# exercise_data = "exercises1.csv"
# exam_points = "exam_points1.csv"

def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1

    return a

def to_points(number):
    return number // 4

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

exams_dict = {}
with open(exam_points) as exam:
    for line in exam:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        parts[1:] = [int(i.strip()) for i in parts[1:]]
        exams_dict[parts[0]] = parts[1:]

with open(course_info) as course:
    course_list = []
    for line in course:
        course_list.append(line.strip().split(':'))
    new_list = [course_list[0][1].strip(), course_list[1][1].strip()]


with open("results.txt", "w") as results, open("results.csv", "w") as stats:
    results.write(f"{new_list[0]}, {new_list[1]} credits\n")
    results.write(f"======================================\n")
    results.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade"}\n")
    for id, name in names.items():
        total = sum(exams_dict[id]) + to_points(sum(exercises[id]))
        results.write(f"{name:30}{sum(exercises[id]):<10}{to_points(sum(exercises[id])):<10}{sum(exams_dict[id]):<10}{total:<10}{grade(total)}\n")
        stats.write(f"{id};{name};{grade(total)}\n")
print(exams_dict)

# print(f"{new_list[0]}, {new_list[1]} credits")
# print("======================================")

# print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade"}")
# for id, name in names.items():
#     total = sum(exams_dict[id]) + to_points(sum(exercises[id]))
#     print(
#         f"{name:30}"
#         f"{sum(exercises[id]):<10}"
#         f"{to_points(sum(exercises[id])):<10}"
#         f"{sum(exams_dict[id]):<10}"
#         f"{total:<10}"
#         f"{grade(total)}"
#         )