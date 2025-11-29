# summation of prime

import math


def sieve(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    d = {k: True for k in range(2, n)}
    for i in range(2, int(math.sqrt(n) + 1)):  # only need to check up to sqrt(n)
        if d[i]:  # the newest prime is the first True value that hasn't been marked
            for j in range(i ** 2, n + 1, i):
                d[j] = False  # mark all multiples of the prime as False (not primes)

    # all True values are primes
    return [k for k, v in d.items() if v is True]


def main(n=10):
    result = sieve(n)
    print(sum(result))


if __name__ == '__main__':
    main(n=2_000_000)
