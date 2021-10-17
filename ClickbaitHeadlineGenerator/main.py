import random
import datetime

OBJECT_PRONOUN = ["Her", "Him", "Them"]
POSSESIVE_PRONOUN = ["Her", "His", "Their"]
PERSONAL_PRONOUN = ["She", "He", "They"]
STATES = [
    "California",
    "Texas",
    "Florida",
    "New York",
    "Pennsylvania",
    "Illinois",
    "Ohio",
    "Georgia",
    "North Carolina",
    "Michigan",
]
NOUNS = [
    "Athlete",
    "Clown",
    "Shovel",
    "Paleo Diet",
    "Doctor",
    "Parent",
    "Cat",
    "Dog",
    "Chicken",
    "Robot",
    "Video Game",
    "Avocado",
    "Plastic Straw",
    "Serial Killer",
    "Telephone Psychic",
]
PLACES = [
    "House",
    "Attic",
    "Bank Deposit Box",
    "School",
    "Basement",
    "Workplace",
    "Donut Shop",
    "Apocalypse Bunker",
]
WHEN = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]


def generate_headline(clickbait_type: int) -> str:
    random.seed(str(datetime.datetime.now()))
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    state = random.choice(STATES)
    place = random.choice(STATES)
    object_pronoun = random.choice(OBJECT_PRONOUN)
    possesive_pronoun = random.choice(POSSESIVE_PRONOUN)
    personal_pronoun = random.choice(PERSONAL_PRONOUN)

    if clickbait_type == 1:
        return f"Are Millenials killing the {noun} industry."
    elif clickbait_type == 2:
        return f"Without this {noun}, {pluralNoun} could kill you {when}."
    elif clickbait_type == 3:
        return f"Big companies hate {object_pronoun}! See how this {state} {noun} invented a cheaper {pluralNoun[:-1]}."
    elif clickbait_type == 4:
        return f"You won't believe what this {state} {noun} found in {possesive_pronoun} {place}."
    elif clickbait_type == 5:
        return f"What {noun+'s'} don't want you to know about {pluralNoun}."
    elif clickbait_type == 6:
        return f"{random.randint(7, 15)} gift ideas to give your {noun} from {state}."
    elif clickbait_type == 7:
        rand_number = random.randint(3, 19)
        return f"{rand_number} reasons why {pluralNoun} are more interesting than you think. (Number {random.randint(1, rand_number)} will suprise you)"
    else:
        return f"This {state} {noun} didn't think robots would take {possesive_pronoun.lower()} job. {personal_pronoun} {'were' if possesive_pronoun == 'Their' else 'was'} wrong."


def main():
    print("Enter the number of clickbait headlines to generate")
    response = ""
    while not response.isdigit():
        response = input("< ")

    number_of_headlines = int(response)

    for i in range(number_of_headlines):
        random.seed(str(datetime.datetime.now()))
        clickbait_type = random.randint(1, 8)
        headline = generate_headline(clickbait_type)
        print(headline)


if __name__ == "__main__":
    main()
