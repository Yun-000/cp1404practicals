from prac_07.guitar import Guitar


def main():
    guitars = []
    add_guitars = []
    filename = 'guitars.csv'

    print("My guitars!")
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        add_guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    write_guitars_to_file(add_guitars, filename)

    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in sorted(guitars):
        print(guitar)


def write_guitars_to_file(guitars, filename):
    with open(filename, 'a') as file:
        for guitar in guitars:
            file.write(f"\n{guitar.name},{guitar.year},{guitar.cost}")


main()
