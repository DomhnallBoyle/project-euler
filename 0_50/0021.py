# amicable numbers

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


def d(n):
    return sum(get_divisors(n))


def main(n=20):
    amicable_numbers = set()

    for a in range(n):
        b = d(a)
        if a == b:
            continue
        c = d(b)
        if c == a:
            amicable_numbers = amicable_numbers.union({a, b})
            
    result = sum(amicable_numbers)
    print(result)


if __name__ == '__main__':
    main(n=10_000)
