from datetime import datetime, timedelta
def screen_time():
    filename = input("Filename: ")
    start_date = datetime.strptime(input("Starting date: "), "%d.%m.%Y")
    print(start_date)
    days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile):")

    # filename = "first_of_may.txt"
    # start_date = datetime.strptime("1.5.2020", "%d.%m.%Y")
    # days = 1
    # screen_report = "30 0 5"
    
    if days == 1:
        end_date = start_date + timedelta(hours=23, minutes=59)
    else:
        end_date = start_date + timedelta(days=days)
    
    

    # print(start_date, end_date)
    result = {}
    # result = {'01.05.2020': '10/10/10', '02.05.2020': '10/10/10'}

    start = start_date
    if (end_date - start_date) < timedelta(days=1) == False:
        screen_report = input(f"Screen time {start.date()}: ")
        result[start.strftime("%d.%m.%Y")] = screen_report.replace(' ', '/')
    else:
        while start <= end_date:
            screen_report = input(f"Screen time {start.date()}: ")
            result[start.strftime("%d.%m.%Y")] = screen_report.replace(' ', '/')
            start += timedelta(days=1)


    with open(filename, "W") as file:
        file.write("")

    # while start <= end_date:
    #     screen_report = input(f"Screen time {start.date()}: ")
    #     result[start.strftime("%d.%m.%Y")] = screen_report.replace(' ', '/')
    #     if days > 1:
    #         start += timedelta(days=1)

    # print(result)

screen_time()