import random
import time


def create_random_number(NUM_DIGITS: int) -> int:
    random.seed(sum(time.gmtime()))
    numbers = list("0123456789")
    random.shuffle(numbers)
    return "".join([num for num in random.sample(numbers, NUM_DIGITS)])


def check_guess_number(random_number: str, guessed_number: str) -> str:

    if random_number == guessed_number:
        return "You got it!"

    for rand, guess in zip(random_number, guessed_number):
        if rand == guess:
            return "Fermi"

    for guess in guessed_number:
        if guess in random_number:
            return "Pico"

    return "Bagels"


if __name__ == "__main__":

    NUM_DIGITS = 3

    while True:

        print(
            """\nI am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues: 
        When I say:         That means:
        Pico                One digit is correct but in wrong position.
        Fermi               One digit is correct and in the right position
        Bagels              No digit is correct"""
        )

        random_number = create_random_number(NUM_DIGITS)
        print("\nI have thought up a number")
        print("You have 10 guesses to get it.")

        for i in range(10):
            print(f"Guess #{i+1}")
            guessed_number = ""
            while len(guessed_number) != 3 or not guessed_number.isdigit():
                guessed_number = input("> ")

            result = check_guess_number(random_number, guessed_number)
            print(result)
            if result == "You got it!":
                break

            elif i == 9:
                print("You ran out of guesses")
                print(f"The answer was {random_number}")

        response = input("Do you want to play again? (yes or no)\n")

        if response == "yes":
            break
        else:
            print("Thanks for playing")
            exit()
