import datetime
import random
from collections import Counter


def birthday_generator(NUM_BIRTHDAYS: int) -> list:
    start_date = datetime.date(year=2018, month=1, day=1)
    birthdays_list = []
    for i in range(NUM_BIRTHDAYS):
        new_date = start_date + datetime.timedelta(days=random.randint(1, 364))
        birthdays_list.append(new_date.strftime("%d %b"))

    return birthdays_list


if __name__ == "__main__":
    print("How many birhdays shall I generate? (max 100)")
    while True:
        NUM_BIRTHDAYS = input("< ")
        if NUM_BIRTHDAYS.isdigit():
            break
    birthdays_list = birthday_generator(int(NUM_BIRTHDAYS))
    print(f"\nHere are {NUM_BIRTHDAYS} birthdays: ")
    print(birthdays_list)

    date, count = Counter(birthdays_list).most_common(1)[0]
    if count > 1:
        print(f"\nMost common birth date is {date}")
    else:
        print("\nThere are no common birth dates")

    print(f"\nGenerating {NUM_BIRTHDAYS} random birthdays 100,000 times....")
    input("Press any key to begin...")

    count_similiar_birthday = 0
    for i in range(0, 100_001):
        if i % 10_000 == 0:
            print("{:,} simulations run...".format(i))

        birthdays_list = birthday_generator(int(NUM_BIRTHDAYS))
        _, count = Counter(birthdays_list).most_common(1)[0]
        if count > 1:
            count_similiar_birthday += 1

    print(
        """\n
        Out of 100,000 simulations of {0} there was matching birthday in
        that group {1} times. This means that {0}
        people have a {2:3.2f} % chance of having a matching
        birthday in their group.""".format(
            NUM_BIRTHDAYS, count_similiar_birthday, count_similiar_birthday / 1000
        )
    )
