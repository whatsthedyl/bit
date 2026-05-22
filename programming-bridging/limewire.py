# q2
from itertools import combinations

def power_set(lst):
    subsets = []
    for r in range(len(lst) + 1):
        subsets.extend(combinations(lst, r))
    return subsets

print(power_set([1, 2, 3]))

# 4
def long_incr_subseq(sequence):
    if not sequence:
        return 0
    numbers = set(sequence)
    longest_streak = 1
    for number in numbers:        
        if number - 1 not in numbers:
            current_streak = 1
            current_number = number
            while current_number + 1 in numbers:
                current_streak += 1
                current_number += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
    return longest_streak