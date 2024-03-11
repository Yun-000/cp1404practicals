colour_to_code = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a',
                  'AliceBlue': '#f0f8ff', 'Alizarin crimson': '#e32636',
                  'Amaranth': '#e52b50', 'Amber': '#ffbf00',
                  'Amethyst': '#9966cc', 'AntiqueWhite': '#faebd7',
                  'Apricot': '#fbceb1', 'Aqua': '#00ffff'}

colour_to_code = {colour.upper(): code for colour, code in colour_to_code.items()}

colour_name = input('Enter a colour name: ').strip().upper()

while colour_name != '':
    if colour_name in colour_to_code:
        print(colour_to_code[colour_name])
    else:
        print('Invalid colour name!')
    colour_name = input('Enter a colour name: ').strip().upper()

print('Farewell')
