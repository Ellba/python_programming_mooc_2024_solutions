# Write your solution here

def process_dict(person):
    results = [value for key, value in person.items() if key.startswith("result")]
    average = sum(results) / len(results)
    return average

def smallest_average(*persons):
    lowest_average_person = None
    lowest_average = float('inf')

    for person in persons:
        average = process_dict(person)

        if average < lowest_average:
            lowest_average = average
            lowest_average_person = person
    
    return lowest_average_person

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    # print(process_dict(person2))
    print(smallest_average(person1, person2, person3))