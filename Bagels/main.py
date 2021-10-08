import random
import time


def create_random_number() -> int:
    random.seed(sum(time.gmtime()))
    return str(random.randint(100, 999))


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

    while True:

        print(
            """\nI am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues: 
        When I say:         That means:
        Pico                One digit is correct but in wrong position.
        Fermi               One digit is correct and in the right position
        Bagels              No digit is correct"""
        )

        random_number = create_random_number()
        print(random_number)
        print("\nI have thought up a number")
        print("You have 10 guesses to get it.")

        for i in range(10):
            print(f"Guess #{i+1}")
            while True:
                guessed_number = input()
                if not guessed_number.isdigit():
                    print("Input is not number")
                elif len(guessed_number) != 3:
                    print("Entered number has more than or less than 3 digits")
                else:
                    break

            result = check_guess_number(random_number, guessed_number)
            print(result)
            if result == "You got it!":
                break

        response = input("Do you want to play again? (yes or no)\n")

        if response == "yes":
            break
        else:
            print("Thanks for playing")
            exit()
