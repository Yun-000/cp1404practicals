"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When an operation receives an argument of a correct type but an invalid value.

2. When will a ZeroDivisionError occur?
Answer: When the program divide a number by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Can, see below.
"""

is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        is_valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")