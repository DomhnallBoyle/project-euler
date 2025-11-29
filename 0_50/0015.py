# lattice paths

import math


def main(n=2):
    # how many permutations of (right, down) among n possible moves?
    num_downs = num_rights = n
    total_moves = num_downs + num_rights
    
    # https://astra-ai.co/videos/combinatorics/permutations/permutations-with-repetition
    num_permutations = math.factorial(total_moves) // (math.factorial(num_downs) * math.factorial(num_rights))
    print(num_permutations)


if __name__ == '__main__':
    main(n=20)
