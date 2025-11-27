# smallest multiple

def main():
    i = 1
    min_int, max_int = 1, 20

    while True:
        if any([i % j != 0 for j in range(min_int, max_int + 1)]):
            i += 1
            continue

        break

    print(i)


if __name__ == '__main__':
    main()
