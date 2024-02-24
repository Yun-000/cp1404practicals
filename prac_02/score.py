"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    print(return_result(score))
    random_score = random.randint(0,101)
    print(f"{random_score:} point, {return_result(random_score):}")

def return_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

if __name__ == "__main__":
    main()

