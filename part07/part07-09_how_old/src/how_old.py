# Write your solution here

from datetime import datetime, timedelta

def how_old():
    millenium = datetime(1999, 12, 31)
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    birthdate = datetime(year, month, day)
    difference = millenium - birthdate
    if difference.days > 0:
        print(f"You were {difference.days} days old on the eve of the new millennium.")
    else: 
        print("You weren't born yet on the eve of the new millennium.")

how_old()