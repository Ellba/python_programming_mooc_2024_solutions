

class Course:
    def __init__(self, name):
        self.__name = name
        self.__course_grade = None
        self.__course_credits = None

    def name(self):
        return self.__name

    def grade(self):
        return self.__course_grade
    
    def credits(self):
        return self.__course_credits

    def set_grade(self, grade):
        self.__course_grade = int(grade)

    def set_credit(self, credit):
        self.__course_credits = int(credit)



class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_grade(self, course_name, course_grade):
        if course_name not in self.__courses:
            self.__courses[course_name] = Course(course_name)
        
        if self.__courses[course_name].grade() is None:
            self.__courses[course_name].set_grade(course_grade)
        elif int(course_grade) > self.__courses[course_name].grade():
            self.__courses[course_name].set_grade(course_grade)
        

    def add_credits(self, course_name, course_credits):
        if course_name not in self.__courses:
            self.__courses[course_name] = Course(course_name)
        self.__courses[course_name].set_credit(course_credits)

    def get_entry(self, course_name):
        if course_name not in self.__courses:
            return None
        # to be removed ---
        # print(
        #     self.__courses[course_name].name(), 
        #     self.__courses[course_name].grade(),
        #     self.__courses[course_name].credits(),
        # )
        # ---
        return self.__courses[course_name]

    
    def statistics(self):
        # 5 completed courses, a total of 29 credits
        # mean 3.4
        # grade distribution
        # 5: xx
        # 4: x
        # 3:
        # 2: x
        # 1: x

        completed_courses = len(self.__courses)
        total_credits = sum(course.credits() for course in self.__courses.values())
        all_grades = [course.grade() for course in self.__courses.values() if course.grade() is not None]
        mean_grade = sum(all_grades) / len(all_grades) if all_grades else 0

        grade_distribution = {grade: all_grades.count(grade) for grade in range(5, 0, -1)}

        print(f"{completed_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")
        for grade in sorted(grade_distribution.keys(), reverse=True):
            print(f"{grade}: {'x' * grade_distribution[grade]}")


class CourseRecordsApplication:
    def __init__(self):
        self.__course_records = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course_data(self):
        course_name = input("course: ")
        course_grade = input("grade: ")
        course_credits = input("credits ")
        
        # here you need to call CourseRecords functions to create Course object and add grades, credits
        self.__course_records.add_grade(course_name, course_grade)
        self.__course_records.add_credits(course_name, course_credits)
        # self.__course_records.get_entry(course_name) # to be removed

    def get_course_data(self):
        course_name = input("course: ")
        data = self.__course_records.get_entry(course_name)
        if data is not None: 
            print(f"{data.name()} ({data.credits()} cr) grade {data.grade()}")
        else:
            print("no entry for this course")

    def get_courses_stats(self):
        return self.__course_records.statistics()
        

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course_data()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_courses_stats()
            else:
                print("Invalid request, stopping application...")
                break

application = CourseRecordsApplication()
application.execute()


"""
add course
    - course name
    - grade
    - credits
    if grade = previous grade:
        previous grade = grade
        credits = credits
get course data
    if no course:
        no entry for this course
statistics
    sum courses, total credits
    mean 
    grade distribution
    5
    4
    3
    2
    1

exit

"""