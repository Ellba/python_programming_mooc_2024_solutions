# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    with open("start_times.csv") as file, open("submissions.csv") as subs:
        start_time = []
        submissions = []
        for line in csv.reader(file, delimiter=';'):
            start_time.append(line)
        for line in csv.reader(subs, delimiter=';'):
            submissions.append(line)
    
    matched = []
    cheaters = []
    for sub in submissions:
        for s in start_time:
            if s[0] == sub[0]:
                start = datetime.strptime(s[1], "%H:%M")
                end = datetime.strptime(sub[3], "%H:%M")
                difference = end - start
                if difference > timedelta(hours=3):
                    cheaters.append(s[0])

    return list(set(cheaters))


if __name__ == "__main__":
    cheaters()