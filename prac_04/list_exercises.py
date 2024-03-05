def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input('Enter the username: ')

    if username in usernames:
        print("Access granted")

        for i in range(5):
            input_number = int(input('Number: '))
            numbers.append(input_number)

        print(f'The first number is {numbers[0]}')
        print(f'The last number is {numbers[-1]}')
        print(f'The smallest number is {min(numbers)}')
        print(f'The largest number is {max(numbers)}')
        print(f'The average of the numbers is {sum(numbers) / len(numbers)}')
    else:
        print("Access denied")


main()