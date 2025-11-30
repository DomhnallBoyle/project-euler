# lexicographic permutations

import itertools


def main(n=1_000_000):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i, permutation in enumerate(itertools.permutations(numbers)):
        if i == n - 1:
            break

    print(''.join([str(x) for x in permutation]))


if __name__ == '__main__':
    main()
