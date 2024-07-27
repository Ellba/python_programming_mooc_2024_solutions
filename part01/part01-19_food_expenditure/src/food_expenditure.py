# Write your solution here
times_cafe = int(input("How many times a week do you eat at the student cafeteria? "))
price_cafe = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
weekly = times_cafe * price_cafe + groceries
daily = weekly/7
print(
    "Average food expenditure:",
    f"\nDaily: {daily} euros",
    f"\nWeekly: {weekly} euros")