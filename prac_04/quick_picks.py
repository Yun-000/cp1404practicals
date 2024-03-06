import random

MIN_NUMBER = 1
MAX_NUMBER = 45


def generate_quick_picks():
    quick_picks = []

    while len(quick_picks) < 6:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_number not in quick_picks:
            quick_picks.append(random_number)

    return sorted(quick_picks)


def main():
    number_of_quick_pick = int(input('How many quick picks? '))

    for i in range(number_of_quick_pick):
        output = generate_quick_picks()
        formatted_output = " ".join(f"{number:2}" for number in output)
        print(formatted_output)


if __name__ == "__main__":
    main()
