# Write your solution here

import urllib.request
import json
import math

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())
    result = []
    for i in data:
        if i["enabled"] == True:
            course_tuple = (
                i['fullName'],
                i['name'],
                int(i['year']),
                int(sum(i['exercises']))
            )
            result.append(course_tuple)

    print(result)
    return result

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(my_request.read())
    students = 0
    hour_total = 0
    exercise_total = 0
    for key, value in data.items():
        if value.get('students') > students:
            students = value.get('students')

        hour_total += value.get('hour_total')
        exercise_total += value.get('exercise_total')
    

    result = {
        'weeks': len(data),
        'students': students,
        'hours': hour_total,
        'hours_average': math.floor(hour_total/students),
        'exercises': exercise_total,
        'exercises_average': math.floor(exercise_total/students),
    }

    print(result)
    return result



if __name__ == "__main__":
    retrieve_course("docker2019")