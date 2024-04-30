import random
import sys
from collections import Counter
from pprint import pprint

N_PAIRS_DEFAULT = 3
N_SIMULATION_RUNS = 1000


def memory_game(n_pairs):
    # Step 1: Create cards
    cards = list(range(1, n_pairs + 1)) * 2
    random.shuffle(cards)
    turns = 1
    unveiled = set()
    
    while cards:
        # print(turns, cards, unveiled)

        # first card
        first = cards.pop()
        if first in unveiled:
            # found a pair
            unveiled.remove(first)
        else:
            # memorize the card
            unveiled.add(first)
            second = cards.pop()
            if second == first:
                # found a pair, great
                unveiled.remove(second)
            elif second in unveiled:
                # found already seen card, takes extra turn to collect it
                unveiled.remove(second)
                turns += 1
            else:
                # no pair
                unveiled.add(second)
                turns += 1
    
    return turns

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n_pairs = int(sys.argv[1])
    else:
        n_pairs = N_PAIRS_DEFAULT
    result = []
    for i in range(N_SIMULATION_RUNS):
        result.append(memory_game(n_pairs))
    pprint(list(sorted(Counter(result).items())))
