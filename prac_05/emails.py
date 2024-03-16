"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email != '':
        name = extract_name(email)
        check = input(f"Is your name {name}? (Y/n) ")
        if check != '' and check.upper() != 'Y':
            name = input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    username = email.split('@')[0]
    name = ' '.join(username.split('.')).title()
    return name


main()