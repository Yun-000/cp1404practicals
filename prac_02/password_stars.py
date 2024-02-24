def main():
    min_length = 8
    password = get_password(min_length)
    print_password(password)

def print_password(password):
    print('*' * len(password))

def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print('Invalid password')
        password = input("Enter password: ")
    return password


if __name__ == "__main__":
    main()


