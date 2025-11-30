# factorial digit sum

def factorial(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1

    return result


def main(n=10):
    n_factorial = factorial(n)
    result = sum([int(d) for d in str(n_factorial)])
    print(result)


if __name__ == '__main__':
    main(n=100)
