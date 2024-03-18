"""
Estimate: 15 minutes
Actual:   13 minutes
"""

from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013)

    print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {12}. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")


main()
