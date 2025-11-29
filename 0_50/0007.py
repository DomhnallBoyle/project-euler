# 10,001st prime

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main(n=6):
    i = 1
    counter = 0
    while counter != n:
        i += 1

        if is_prime(i):
            counter += 1

    print(i)


if __name__ == '__main__':
    main(n=10_001)
