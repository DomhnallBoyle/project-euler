# largest prime factor

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


def main():
    n = 600851475143
    max_divisor = n

    for i in range(1, max_divisor + 1):
        m = n / i
        if not m.is_integer():
            continue

        if is_prime(int(m)):
            break

    print(int(m))


if __name__ == '__main__':
    main()
