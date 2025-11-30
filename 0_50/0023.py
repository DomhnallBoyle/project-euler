# non-abundant sums

divisors_d = {}


def get_divisors(n):
    # use any cached divisors
    if n in divisors_d:
        return divisors_d[n]

    _max = n // 2
    divisors = []
    for i in range(1, _max + 1):
        if n % i == 0:
            divisors.append(i)
    
    # cache divisors
    divisors_d[n] = set(divisors)
    divisors_reversed = divisors.copy()[::-1]
    for i in range(len(divisors_reversed) - 1):
        n = divisors_reversed[i]
        divisors_d[n] = set(divisors_reversed[i + 1:])

    return set(divisors)


def main():
    limit = 28123

    # first find all abundant numbers
    abundant_numbers = []
    for n in range(limit):
        divisors = get_divisors(n)
        if sum(divisors) <= n:
            continue
        abundant_numbers.append(n)

    # calculate all sum combinations of abundant numbers - keep unique
    sum_of_abundant_numbers = set()
    for i in range(len(abundant_numbers) - 1):
        for j in range(i, len(abundant_numbers)):
            a, b = abundant_numbers[i], abundant_numbers[j]
            sum_of_abundant_numbers.add(a + b)            

    # set difference to find leftovers
    sum_non_abundant_numbers = set(range(limit)) - sum_of_abundant_numbers
    print(sum(sum_non_abundant_numbers))


if __name__ == '__main__':
    main()
