def collatz_sequence_generator(number: int) -> list:
    sequence = []
    sequence.append(number)

    if number == 1:
        return sequence

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        sequence.append(number)

    return sequence


def main():
    print(
        "The Collatz Generator is a sequence of numbers produced from a starting number n, following three rules:"
    )
    print("1. If n is even, the next number n is n / 2.")
    print("2. If n is odd, the next number n is n * 3 + 1.")
    print("3. If n is 1, stop. Otherwise, repeat.")
    print()
    print("Enter a starting number (greater than 0) or (Q)UIT:")
    while True:
        response = input("< ")
        if response.upper() in ["QUIT", "Q"]:
            exit()

        elif response.isdigit():
            if int(response) > 0:
                number = int(response)
                break

    collatz_sequence = collatz_sequence_generator(number)
    print(*collatz_sequence)


if __name__ == "__main__":
    main()
