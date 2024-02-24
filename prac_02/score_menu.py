def main():
    score = int(input('Enter a valid score (0-100): '))
    while score < 0 or score > 100:
        print("You enter an invalid score.")
        score = int(input('Enter a valid score (0-100): '))

    print("(G)et a valid score (must be 0-100 inclusive)\n"
          "(P)rint result (copy or import your function to determine the result from sco"
          "re.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit:")
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'G':
            score = int(input('Enter a valid score (0-100): '))
            while score < 0 or score > 100:
                print("You enter an invalid score.")
                score = int(input('Enter a valid score (0-100): '))
        elif choice == 'P':
            print(return_result(score))
        elif choice == 'S':
            print('*' * len(str(score)))
        else:
            print('Invalid choice')
        print("(G)et a valid score (must be 0-100 inclusive)\n(P)rint resu"
              "lt (copy or import your function to determine the result from"
              " score.py)\n(S)how stars (this should print as many stars as"
              " the score)\n(Q)uit:")
        choice = input('>>> ').upper()
    print('Farewell.')

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