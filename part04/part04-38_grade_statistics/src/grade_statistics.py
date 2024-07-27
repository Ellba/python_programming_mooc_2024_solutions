
"""
1. User inputs exam points - integers between 0 and 20 and the number of exercises completed - an integer between 0 and 100.
2. Keep asking for input until the user types in an empty line. 
3. Completing at least 10% of the exercises grants one point, 20% grants two points... 
    The number of exercise points granted is an integer value, rounded down.
4. 
    exam points + exercise points	grade
    0-14	0 (i.e. fail)
    15-17	1
    18-20	2
    21-23	3
    24-27	4
    28-30	5
5. If a student received less than 10 points from the exam, they automatically fail the course, 
    regardless of their total number of points.
6. Floating point numbers should be printed out with one decimal precision.

Example:

Statistics:
Points average: 14.5
Pass percentage: 75.0
Grade distribution:
  5:
  4:
  3: *
  2:
  1: **
  0: *


Example of the task solution:
1. input_from_user
    collect input and place it into list
2. print_result
    print all number in collected list
3. analyze
    process data, return calculations


Task solution breakdown:
1. input_from_user
    collect input
    separate into list pairs in main list
    return main list
2. prepare data
    convert strings in pair lists into integers
    collect exercise points into list: integer value, rounded down
    collect exam points
    collect sum_points: exercise + exam points
3. analyze
    calculate average from sum_points: float 1 decimal
    calculate grades from sum_points: return grade distribution list
    calculate pass percentage from grade distribution list
4. print results
    average
    pass percentage
    grade distribution
"""



def input_from_user():
    result = []

    # collect input
    while True:
        scores = input("Exam points and exercises completed: ")       
        if scores == "":
            break 
        
        result.append(scores.split(" ", 1))   
    converted = converter(result)

    return result


def converter(result):
    
    for pair in result:
        for num in range(len(pair)):
            pair[num] = int(pair[num])
        pair[1] = pair[1]//10
        pair.append(sum(pair))
    
    return result


def average(result):
    sum_plus = 0
    for pair in result:
        sum_plus += pair[2]
    
    points_average = round(sum_plus/len(result),1)
    return points_average


def grades(result):
    grade_list = [0,0,0,0,0,0]

    for i in result:
        if i[0] < 10 or i[2] in range(0, 15):
            grade_list[0] += 1      
        elif i[2] in range(15, 18):
            grade_list[1] += 1 
        elif i[2] in range(18, 21):
            grade_list[2] += 1
        elif i[2] in range(21, 24):
            grade_list[3] += 1
        elif i[2] in range(24, 28):
            grade_list[4] += 1
        elif i[2] in range(28, 31):
            grade_list[5] += 1
    
    return grade_list


def print_result(result, grade_list):
    points_average = average(result)
    
    grades_sum = 0
    for i in grade_list[1:]:
        grades_sum += i
    
    pass_percentage = grades_sum/sum(grade_list)*100

    print(
        "Statistics:",
        f"\nPoints average: {points_average}",
        f"\nPass percentage: {pass_percentage:.1f}",
        f"\nGrade distribution:"
        )

    n = len(grade_list)-1
    for i in grade_list[::-1]:
        print(f"  {n}: {i*"*"}")
        n -= 1



def main():
    result = input_from_user()
    grade_result = grades(result)
    print_result(result, grade_result)

main()

"""
DEFAULT SOLUTION

def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()

"""

# GPT SOLUTION

# def calculate_statistics(scores):
#     """
#     Calculates average points and grade distribution from processed scores.
#     """
#     if not scores:
#         return 0, [0] * 6
    
#     average_points = round(sum(total for _, _, total in scores) / len(scores), 1)
    
#     grade_distribution = [0] * 6
#     for exam, _, total in scores:
#         if exam < 10 or total < 15:
#             grade_distribution[0] += 1
#         else:
#             grade_index = min((total - 15) // 3, 4) + 1
#             grade_distribution[grade_index] += 1
            
#     return average_points, grade_distribution

# def display_statistics(average_points, grade_distribution):
#     """
#     Displays the calculated statistics.
#     """
#     pass_count = sum(grade_distribution[1:])
#     pass_percentage = (pass_count / sum(grade_distribution) * 100) if grade_distribution else 0
#     print("Statistics:",
#           f"\nPoints average: {average_points}",
#           f"\nPass percentage: {pass_percentage:.1f}%",
#           "\nGrade distribution:")
#     for grade, count in enumerate(grade_distribution[::-1], start=1):
#         print(f"  {6-grade}: {count * '*'}")

# def main():
#     scores = get_user_input()
#     processed_scores = process_scores(scores)
#     average_points, grade_distribution = calculate_statistics(processed_scores)
#     display_statistics(average_points, grade_distribution)

# if __name__ == "__main__":
#     main()
