import random


def generate_die_roll(rolls: int, die_face: int, extra: str, sign: str) -> list[int]:
    output = []
    for i in range(rolls):
        output.append(random.randint(1, die_face))

    if sign is not None:
        if sign == "-":
            output.append(int(extra) * -1)
        else:
            output.append(int(extra))

    return sum(output), output


def main():
    print("Enter the die roll required:")
    while True:
        die_roll = input("< ")
        if "d" in die_roll and len(die_roll) > 2:
            rolls, die = die_roll.split("d")
            if rolls.isdigit() and isinstance(eval(die), int):
                break

    extra, sign = None, None
    if "-" in die:
        die, extra = die.split("-")
        sign = "-"

    elif "+" in die:
        die, extra = die.split("+")
        sign = "+"

    total_sum, each_roll = generate_die_roll(int(rolls), int(die), extra, sign)
    print(total_sum, each_roll)


if __name__ == "__main__":
    main()
