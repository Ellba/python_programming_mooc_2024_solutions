from datetime import datetime, timedelta
def screen_time():
    filename = input("Filename: ")
    start_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
    print(start_date)
    days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile):")

    if days == 1:
        end_date = start_date + timedelta(hours=23, minutes=59)
    else:
        days -= 1
        end_date = start_date + timedelta(days=days)
    
    print(start_date, end_date)

    result = {}

    start = start_date
    if (end_date - start_date) < timedelta(days=1) == False:
        screen_report = input(f"Screen time {start.date()}: ")
        result[start.strftime("%d.%m.%Y")] = screen_report.replace(' ', '/')
    else:
        while start <= end_date:
            screen_report = input(f"Screen time {start.date()}: ")
            result[start.strftime("%d.%m.%Y")] = screen_report.replace(' ', '/')
            start += timedelta(days=1)


    total_minutes = 0
    for key, value in result.items():
        total_minutes += eval(value.replace('/', '+'))
    
    average_minutes = round(total_minutes/len(result), 2)
    print(start_date, end_date)

    with open(filename, "w") as file:
        file.write(f"Time period: {start_date.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n")
        file.write(f"Total minutes: {total_minutes}\n")
        file.write(f"Average minutes: {average_minutes}\n")
        for key, value in result.items():
            file.write(f"{key}: {value}\n")


screen_time()
