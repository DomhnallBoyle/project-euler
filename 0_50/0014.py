# largest collatz sequence

def next_value(n):
    if n % 2 == 0:
        return int(n / 2)
    
    return (3 * n) + 1


def main(max_start=1_000_000):
    chains_d = {}

    for starting_number in range(max_start, 1, -1):
        chain = [starting_number]
        n = starting_number
        while n != 1:
            chain_history = chains_d.get(n)
            if chain_history is not None:
                chain.extend(chain_history)
                break

            n = next_value(n)
            chain.append(n)

        for i in range(len(chain) - 1):
            if chain[i] in chains_d:
                continue
            chains_d[chain[i]] = chain[i + 1:]

    result = max(chains_d.items(), key=lambda x: len(x[1]))
    print(result[0], len(result[1]))


if __name__ == '__main__':
    main()
