# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    result = json.loads(data)
    
    for student in result:
        print(f"{student['name']} {student['age']} years ({', '.join(student['hobbies'])})")

if __name__ == "__main__":
    print_persons("file1.json")