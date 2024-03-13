"""
Word Occurrences
Estimate: 35 minutes
Actual:   30 minutes
"""


def main():
    filename = '/Users/luol./Downloads/wimbledon.csv'
    data = read_file(filename)
    champion_to_win = find_champion(data)
    countries = find_country(data)

    print("Wimbledon Champions: ")
    for champion, wins in champion_to_win.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(', '.join(sorted(countries)))


def read_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            row = line.strip().split(',')
            data.append(row)
    return data


def find_champion(data):
    champion_to_win = {}
    for row in data[1:]:
        champion = row[2]
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win


def find_country(data):
    countries = set()
    for row in data[1:]:
        countries.add(row[3])
    return countries


main()
