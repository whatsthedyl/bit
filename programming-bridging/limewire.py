# q2
from itertools import combinations

def power_set(lst):
    subsets = []
    for r in range(len(lst) + 1):
        subsets.extend(combinations(lst, r))
    return subsets

print(power_set([1, 2, 3]))