import random


def main():
    JAPANESE_NUMBERS = {1: "ICHI", 2: "NI", 3: "SAN", 4: "SHI", 5: "GO", 6: "ROKU"}
    print(
        """In this traditional Japanese dice game, two dice are rolled in a bamboo cup
        by the dealer sitting on the floor. The player must guess if the dice total to
        an even (cho) or odd (han) number."""
    )

    money = 5000

    while money > 0:
        print(f"You have {money} mon. How much do you bet? (or QUIT)")
        bet = ""
        while not bet.isdigit():
            bet = input("< ").upper()
            if bet == "QUIT":
                exit()

        print(
            """The dealer swirls the cup and you hear the rattle of dice.
        The dealer slams the cup on the floor,
        still covering the dice and asks for bet"""
        )
        print("CHO (even) or HAN (odd) ?")
        response = ""
        while response not in ["CHO", "HAN"]:
            response = input("< ").upper()

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("The dealer lifts the cup to reveal:")
        print(
            "{0: ^10} - {1: ^10}".format(
                JAPANESE_NUMBERS[dice1], JAPANESE_NUMBERS[dice2]
            )
        )
        print("{0: ^10} - {1: ^10}".format(dice1, dice2))

        if ((dice1 + dice2) % 2 == 0 and response == "CHO") or (
            (dice1 + dice2) % 2 == 1 and response == "HAN"
        ):
            print(f"You won! You take {int(bet)*2} mon.")
            money += int(bet) * 2
            print(f"The house collects a {int(bet)//2} mon fee.")
            money -= int(bet) // 2

        else:
            money -= int(bet)
            print(f"You lost. You lose {bet} money")

    print("You have run out of money!")
    print("Thanks for playing")


if __name__ == "__main__":
    main()
