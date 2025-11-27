# Largest Palindrome Product

def is_palindrome(n):
    n = str(n)

    return n == n[::-1]


def main():
    max_int = 999
    min_int = 100
    largest_palindrome_product = 0

    for n in range(max_int, min_int - 1, -1):
        for m in range(max_int, min_int - 1, -1):
            product = n * m
            if is_palindrome(product) and product > largest_palindrome_product:
                largest_palindrome_product = product

    print(largest_palindrome_product)


if __name__ == '__main__':
    main()
