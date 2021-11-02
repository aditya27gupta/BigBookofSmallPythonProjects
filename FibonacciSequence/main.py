#!usr/bin/python3


def fibonacci_sequence(num: int) -> list:
    sequence = [0, 1]

    if num == 1:
        return sequence[0]
    elif num == 2:
        return sequence
    else:
        for i in range(2, num):
            next_num = sequence[i-2] + sequence[i-1]
            sequence.append(next_num)

    return sequence


def main():
    print("Enter the Nth Fibonacci number you wish to calculate")
    num = ''
    while not num.isdigit():
        num = input("< ")

    result = fibonacci_sequence(int(num))
    print(result)


if __name__ == "__main__":
    main()
