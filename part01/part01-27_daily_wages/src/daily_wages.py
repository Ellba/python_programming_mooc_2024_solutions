# Write your solution here
hour_wage = float(input("Hourly wage: "))
hour_worked = float(input("Hours worked: "))
day = input("Day of the week: ")
daily_wages = hour_wage * hour_worked
if day == "Sunday":
    daily_wages *= 2
print(f"Daily wages: {daily_wages} euros")