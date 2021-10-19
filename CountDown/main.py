import time
import os


def print_watch(hrs: int, mins: int, secs: int):
    seven_segment = {
        "0": [" -- ", "|  |", "|  |", " -- "],
        "1": ["    ", "  | ", "  | ", "    "],
        "2": [" -- ", " __|", "|   ", " -- "],
        "3": [" -- ", " __|", "   |", " -- "],
        "4": ["    ", "|__|", "   |", "    "],
        "5": [" -- ", "|__ ", "   |", " -- "],
        "6": [" -- ", "|__ ", "|  |", " -- "],
        "7": [" -- ", "   |", "   |", "    "],
        "8": [" -- ", "|__|", "|  |", " -- "],
        "9": [" -- ", "|__|", "   |", " -- "],
    }

    hrs = "0" + str(hrs) if len(str(hrs)) < 2 else str(hrs)
    mins = "0" + str(mins) if len(str(mins)) < 2 else str(mins)
    secs = "0" + str(secs) if len(str(secs)) < 2 else str(secs)

    for i in range(4):
        if i not in (1, 2):
            print(
                "{} {}   {} {}   {} {}".format(
                    seven_segment[hrs[0]][i],
                    seven_segment[hrs[1]][i],
                    seven_segment[mins[0]][i],
                    seven_segment[mins[1]][i],
                    seven_segment[secs[0]][i],
                    seven_segment[secs[1]][i],
                )
            )
        else:
            print(
                "{} {} * {} {} * {} {}".format(
                    seven_segment[hrs[0]][i],
                    seven_segment[hrs[1]][i],
                    seven_segment[mins[0]][i],
                    seven_segment[mins[1]][i],
                    seven_segment[secs[0]][i],
                    seven_segment[secs[1]][i],
                )
            )


def update_time(hrs: int, mins: int, secs: int) -> (int, int, int):
    if secs == 0:
        secs = 59
        if mins == 0:
            mins = 59
            hrs -= 1
        else:
            mins = 0
    else:
        secs -= 1

    return hrs, mins, secs


def main():
    print("Enter the time for countdown:")

    while True:
        hours = input("Hours (0-11) > ")
        if hours.isdigit():
            if int(hours) in range(0, 12):
                break

    while True:
        minutes = input("Minutes (0-59) > ")
        if minutes.isdigit():
            if int(minutes) in range(0, 60):
                break

    while True:
        seconds = input("Seconds (0-59) > ")
        if seconds.isdigit():
            if int(seconds) in range(0, 60):
                break

    hours, minutes, seconds = int(hours), int(minutes), int(seconds)

    while not (hours == 0 and minutes == 0 and seconds == 0):
        print_watch(hours, minutes, seconds)
        hours, minutes, seconds = update_time(hours, minutes, seconds)
        print()
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
