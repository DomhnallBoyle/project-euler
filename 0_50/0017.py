# number letter counts

def main(n=5):
    units_to_letters_d = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    tens_to_letters_d = {
        '0': '',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }

    letters_total = ''

    for number in range(1, n + 1):
        letters = ''
        number = str(number)

        if len(number) == 4:
            letters = f'{units_to_letters_d[number[0]]}thousand'
        elif len(number) >= 2:
            hundreds, tens, units = number.zfill(3)
            if tens == '0':
                letters = units_to_letters_d[units]
            elif tens == '1':
                letters = units_to_letters_d[f'{tens}{units}']
            else:
                letters = f'{tens_to_letters_d[tens]}{units_to_letters_d[units]}'

            if len(number) == 3:
                prefix = f'{units_to_letters_d[hundreds]}hundred'
                if letters:
                    prefix += f'and{letters}'
                letters = prefix
        else:
            letters = units_to_letters_d[number[0]]

        letters_total += letters

    letter_count = len(letters_total)
    print(letter_count)


if __name__ == '__main__':
    main(n=1000)
