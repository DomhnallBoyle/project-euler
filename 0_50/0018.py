# maximum path sum 1

def main():
    # triangle = '''
    #     3
    #     7 4
    #     2 4 6
    #     8 5 9 3
    # '''
    triangle = '''
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''

    numbers_2d = []
    for line in triangle.splitlines():
        line = line.strip()
        if not line:
            continue
        numbers = [int(number) for number in line.split(' ')]
        numbers_2d.append(numbers)

    # start from the bottom, eliminating as many paths as possible
    # total up the neighbours from the previous row, keeping the max
    # repeat all the way to the top
    # the top value should be the max_total path

    def process_row(row_number):
        if row_number == -1:
            return
        
        previous_row_number = row_number + 1
        numbers = numbers_2d[row_number]
        new_numbers = []
        for number_index, number in enumerate(numbers):
            i = number_index
            j = number_index + 1
            new_number = max(number + numbers_2d[previous_row_number][i], number + numbers_2d[previous_row_number][j])
            new_numbers.append(new_number)
        
        numbers_2d[row_number] = new_numbers
        process_row(row_number - 1)

    num_rows = len(numbers_2d)
    process_row(num_rows - 2)

    max_total = numbers_2d[0][0]
    print(max_total)


if __name__ == '__main__':
    main()
