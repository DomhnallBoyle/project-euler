# power digit sum

def main(n=15):
    digits = 2 ** n
    result = sum([int(d) for d in str(digits)])
    print(result)


if __name__ == '__main__':
    main(n=1000)
