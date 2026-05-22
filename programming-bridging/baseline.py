# 2
def longest_consecutive_sequence(numbers):
    if not numbers:
        return 0
    numbers = set(numbers)
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

# 3
import numpy as np

def calculate_standardized_scores(scores):
    scores = np.array(scores)
    return (scores - scores.mean(axis=1, keepdims=True)) / scores.std(axis=1, keepdims=True)

# 4
def rearrange_exponential_increase(vals):
    length = len(vals)
    if length <= 1:
        return vals

    vals = sorted(vals)
    for index in range(1, length):
        if vals[index] <= 2 * vals[index - 1]:
            return []

    return vals