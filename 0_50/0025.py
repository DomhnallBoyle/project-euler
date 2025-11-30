# 1000-digit fibonacci number

def main(n=3):
    index = 1
    prev_prev = 0
    prev = 1

    while True:
        fib_term = prev_prev + prev
        index += 1

        if len(str(fib_term)) == n:
            break

        prev_prev = prev
        prev = fib_term
    
    print(index, fib_term)


if __name__ == '__main__':
    main(n=1000)
