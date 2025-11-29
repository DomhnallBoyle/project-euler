# special pythagorean triplet

def main(n=25):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if not (a < b < c) or not (a + b + c) == n:
                    continue

                if (a ** 2) + (b ** 2) == (c ** 2):
                    return a, b, c


if __name__ == '__main__':
    a, b, c = main(n=1000)
    print(a, b, c)
    print(a * b * c)
