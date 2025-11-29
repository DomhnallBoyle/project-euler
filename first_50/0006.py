# sum square difference

def main(n=10):
    sum_of_squares = sum([i ** 2 for i in range(1, n + 1)])
    square_of_sums = sum([i for i in range(1, n + 1)]) ** 2

    diff = square_of_sums - sum_of_squares
    print(diff)


if __name__ == '__main__':
    main(n=100)
