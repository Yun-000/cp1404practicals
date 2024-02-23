def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print('Invalid password')
        password = input("Enter password: ")
    return password

min_length = 8

password = get_password(min_length)

print('*' * len(password))
