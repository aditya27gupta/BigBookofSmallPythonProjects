#!/usr/bin/python3

import math


def find_factor(num: int) -> list:

    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)

    return sorted(factors)


def main():
    num = ""
    while not num.isdigit():
        print("Enter a number to factor")
        num = input("< ")

    factors = find_factor(int(num))
    print(factors)


if __name__ == "__main__":
    main()
