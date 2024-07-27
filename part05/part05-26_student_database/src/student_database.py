# Write your solution here

def add_student(students, name): 
    students[name] = {}

def print_student(students, name):    
    average = 0
    if name in students:
        if students[name]:
            print(f"{name}: \n {len(students[name])} completed courses:")
            for course, grade in students[name].items():
                average += grade    
                print(f"  {course} {grade}")
            print(f" average grade {average/len(students[name])}")
        
        else:
            print(f"{name}: \n no completed courses")
    else:
        print(f"{name}: no such person in the database")


def add_course(students, name, course: tuple):
    course_name, grade = course
    if grade > 0:
        if name in students:
            if course_name not in students[name] or grade > students[name][course_name]:
                students[name][course_name] = grade

def summary(students):
    # most courses completed 3 Peter
    # best average grade 4.5 Eliza

    max_courses = 0
    student_most_courses = None
    for student, courses in students.items():
        if len(courses) > max_courses:
            max_courses = len(courses)
            student_most_courses = student

    best_average = 0
    student_best_average = None
    for student, courses in students.items():
        total_grade = sum(courses.values())
        num_courses = len(courses)
        average_grade = total_grade / num_courses if num_courses else 0
        if average_grade > best_average:
            best_average = average_grade
            student_best_average = student


    print(f"students {len(students)}")
    print(f"most courses completed {max_courses} {student_most_courses}")
    print(f"best average grade {best_average} {student_best_average}")



    


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
