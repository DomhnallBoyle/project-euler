# highly divisible triangular number

import math


def generate_triangle_number():
    i = 0
    add_term = 1

    while True:
        i += add_term
        add_term += 1

        yield i


def get_divisors(n):
    # a fast way to get divisors is treat it like pairs of factors
    # if n = 28, pairs of factors are 1 & 28, 2 & 14, 4 & 7
    # do this all the way up to the square root
    divisors = []

    for i in range(1, int(math.sqrt(n))):
        x = n / i
        if x != int(x):
            continue
        divisors.extend([i, x])

    return divisors


def main():
    divisor_d = {}

    for i, num in enumerate(generate_triangle_number()):
        divisors = get_divisors(num, divisor_d)

        if i == 6:
            assert set(divisors) == {1, 2, 4, 7, 14, 28}, divisors

        if len(divisors) > 500:
            break

    print(num)


if __name__ == '__main__':
    main()
