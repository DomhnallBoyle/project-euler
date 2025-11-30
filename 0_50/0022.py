# names scores

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    with open('names.txt', 'r') as f:
        names = f.read().replace('"', '').split(',')
    
    names = sorted(names)

    total_score = 0
    for i, name in enumerate(names):
        name_score = sum([alphabet.index(letter) + 1 for letter in name.lower()]) * (i + 1)
        total_score += name_score

    print(total_score)


if __name__ == '__main__':
    main()
