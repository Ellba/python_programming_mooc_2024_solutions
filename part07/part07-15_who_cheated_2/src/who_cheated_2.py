# Write your solution here

import csv
from datetime import datetime, timedelta

def final_points():
    with open("start_times.csv") as file, open("submissions.csv") as subs:
        start_time = []
        submissions = []
        for line in csv.reader(file, delimiter=';'):
            start_time.append(line)
        for line in csv.reader(subs, delimiter=';'):
            submissions.append(line)
    
    start_time_format = "%H:%M"
    start_time_dict = {name: datetime.strptime(time_str, start_time_format).time() for name, time_str in start_time}

    # Nested dictionary to keep track of the highest score for each task for each student
    student_task_scores = {}
    for submission in submissions:
        student, task, score, submit_time = submission
        score = int(score)

        # Convert submit_time to datetime.time object
        submit_time_dt = datetime.strptime(submit_time, start_time_format).time()

        # Get the start time for the student
        if student in start_time_dict:
            student_start_time = start_time_dict[student]
        else:
            continue  # Skip if the student's start time is not found

        # Calculate time difference
        start_datetime = datetime.combine(datetime.today(), student_start_time)
        submit_datetime = datetime.combine(datetime.today(), submit_time_dt)
        time_difference = submit_datetime - start_datetime

        # Ignore submissions made over 3 hours after the start time
        if time_difference > timedelta(hours=3):
            continue

        # Initialize the dictionary for the student if not already present
        if student not in student_task_scores:
            student_task_scores[student] = {str(i): 0 for i in range(1, 9)}

        # Update the highest score for the task if the current score is higher
        if score > student_task_scores[student][task]:
            student_task_scores[student][task] = score

    # Calculate the total points for each student
    final_scores = {student: sum(scores.values()) for student, scores in student_task_scores.items()}

    print(final_scores)
    return final_scores

if __name__ == "__main__":
    final_points()