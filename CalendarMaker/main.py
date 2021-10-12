import datetime


def get_calendar_dates(year: int, month: int) -> (int, int, str):
    total_days = 0
    start_date = datetime.date(year, month, day=1)
    weekday = start_date.weekday()
    month_name = start_date.strftime("%B")

    for i in range(31):
        total_days += 1
        next_date = start_date + datetime.timedelta(days=1)
        if next_date.month != month:
            break
        start_date = next_date

    return total_days, weekday, month_name


def create_calendar(total_days: int, start_week_day: int, month_name: str, year: int):
    print("{0:>41} {1:41}".format(month_name, year))
    weekdays = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]

    for week in weekdays:
        print("{:.^12}".format(week), end="")
    print()

    start_date = 1
    weekday_check = 0
    while start_date <= total_days:
        for i in range(7):
            if i == 6:
                print("+..........+")
            else:
                print("+...........", end="")

        for i in range(7):
            if i == 6:
                print("|          |")
            else:
                print("|           ", end="")

        for i in range(7):
            if weekday_check < start_week_day:
                print("|           ", end="")
                weekday_check += 1
            elif i == 6:
                print("|    {: <2}    |".format(start_date))
                start_date += 1
            else:
                print("|    {: <2}     ".format(start_date), end="")
                start_date += 1

        for i in range(7):
            if i == 6:
                print("|          |")
            else:
                print("|           ", end="")

    for i in range(7):
        if i == 6:
            print("+..........+")
        else:
            print("+...........", end="")


def main():
    year, month = "", ""

    print("Enter the year for the calendar:")
    while not year.isdigit() or not len(year) == 4:
        year = input("< ")

    print("Enter the month for the calendar, 1-12:")
    while True:
        month = input("< ")
        if not month.isdigit():
            print("Enter a numerical value")
        elif int(month) < 1 or int(month) > 12:
            print("Enter value between 1 and 12")
        else:
            break

    total_days, start_week_day, month_name = get_calendar_dates(int(year), int(month))
    create_calendar(total_days, start_week_day, month_name, year)


if __name__ == "__main__":
    main()
