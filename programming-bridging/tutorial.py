# 1
def max_min(lst):
    return (max(lst, default=None), min(lst, default=None))

# 2
# question constraint if-elif-else
def describe_day(temperature):
    if temperature < 0:
        description = 'Very Cold'
    elif temperature <= 10:
        description = 'Cold'
    elif temperature <= 20:
        description = 'Moderate'
    elif temperature <= 30:
        description = 'Warm'
    else: 
        description = 'Hot'
    
    return description

# 3
# cringe method
def calculate_bmi(weight, height):
    return f"BMI is {(bmi := round(weight / (height ** 2), 2))}, you are {("underweight", "normal weight", "overweight", "obese")[(bmi >= 18.5) + (bmi >= 24.9) + (bmi >= 29.9)]}."

# readable
def calculate_bmi(weight, height):
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 24.9:
        category = "normal weight"
    elif bmi < 29.9:
        category = "overweight"
    else:
        category = "obese"        

    return f"BMI is {bmi}, you are {category}."

# 4
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# 5
# longest but algorithmically fastest
def max_min_odd(lst):
    max_odd = min_odd = None
    for number in lst:
        if number % 2:
            if max_odd is None or number > max_odd:
                max_odd = number
            if min_odd is None or number < min_odd:
                min_odd = number
                
    return (max_odd, min_odd)

# concise but less efficient
def max_min_odd(lst):
    return (max(odd_numbers := [number for number in lst if number % 2], default=None), min(odd_numbers, default=None))

# same as above but more readable
def max_min_odd(lst):
    odd_numbers = [number for number in lst if number % 2]
    return (max(odd_numbers, default=None), min(odd_numbers, default=None))

# 6
def concat_unique(lst1, lst2):
    seen = set(lst1)
    for element in lst2:
        if element not in seen:
            lst1.append(element)
            seen.add(element)
    
    return lst1;

# 7
# by right should convert to integer cents to avoid float precision issues
def coin_change(price, received):
    denominations = [1, 0.5, 0.2, 0.1]
    change = received - price
    if change == 0:
        return []
    
    change_coins = []
    for denomination in denominations:
        quotient, remainder = divmod(change, denomination)
        change_coins.extend([denomination] * quotient)
        if remainder == 0:
            break
     
    return change_coins

# 8
def courses_only_A(a_courses, b_courses):
    return list(set(a_courses) - set(b_courses))

# 9
# question constraint while
def while_7_odd(lst):
    odd_numbers = []
    index = 0
    while index < len(lst):
        if lst[index] % 2:
            odd_numbers.append(lst[index])
        if len(odd_numbers) == 7:
            break
        index += 1
    return odd_numbers

# 10
# question constraint for
def for_7_odd(lst):
    odd_numbers = []
    odd_number_count = 0
    for number in lst:
        if number % 2:
            odd_numbers.append(number)
            odd_number_count += 1
        if odd_number_count == 7:
            break
    
    return odd_numbers

# 11
def count_vowels(s):
    return sum(char in {"a", "e", "i", "o", "u"} for char in s.lower())
    
# 12
# does not handle win_size > lst length
# question constraint slicing
def window_avg(lst, win_size):
    length = len(lst)
    end_index = len(lst) - 1
    averages = []
    for index in range(len(lst)):
        window_end_index = index + win_size - 1
        if window_end_index > end_index:
            demands = lst[index:] + lst[:window_end_index % length + 1]
        else:
            demands = lst[index:window_end_index + 1]
        print(demands)
        averages.append(round(sum(demands) / win_size, 1))
    return averages

# 13
def rearrange_by_length(s):
    return " ".join(sorted(s.split(" "), key=len))

# 14
# because first word chars guaranteed unique
def merge_strings(words):
    return "".join(dict.fromkeys("".join(words)))

# 15
def word_lengths(s, delimiters):
    delimiters = set(delimiters)
    lengths = []
    current_length = 0
    for char in s:
        if char in delimiters:
            if current_length:
                lengths.append(current_length)
                current_length = 0
        else:
            current_length += 1
    if current_length:
        lengths.append(current_length)
    return lengths

# 16
def f(s):
    return "".join([("-", "C", "V")[("a" <= char <= "z" or "A" <= char <= "Z") + (char in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"})] for char in s])

# 17
# question constraints
def count_letters(sentence):
    letters = {}
    for char in sentence.lower():
        if "a" <= char <= "z":
            letters[char] = letters.get(char, 0) + 1
    return letters
    
# 40
# question constraint loops, otherwise just find highest positive/lowest negative pair
from itertools import combinations

def find_max_product_pair(numbers):
    if len(numbers) < 2:
        return ()
    combos = combinations(numbers, 2)
    max_product = 0
    max_pair = ()
    for num1, num2 in combos:
        product = num1 * num2
        if product > max_product:
            max_product = product
            max_pair = (num1, num2)
    return max_pair

# 41
def deep_copy_2d(lst):
    return [[item for item in l] for l in lst]

# 42
def zigzag_fill(s):
    if not s:
        return [[]]
        
    n = 1
    while n ** 2 < len(s):
        n += 1

    grid = [[" "] * n for _ in range(n)]
    for index, char in enumerate(s):
        row = index // n
        col = index % n
        if row % 2 == 1:
            col = n - 1 - col
        grid[row][col] = char
        print(grid)
        
    return grid

# 43
from sympy import isprime
import math

def gcd_of_non_primes(numbers):
    non_primes = [number for number in numbers if not isprime(number)]
    if not non_primes:
        return -1
    return math.gcd(*non_primes)

# no libraries
def gcd_of_non_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for d in range(3, int(n ** 0.5) + 1, 2):
            if n % d == 0:
                return False
        return True
        
    non_primes = [number for number in numbers if not is_prime(number)]
    if not non_primes:
        return -1
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = non_primes[0]
    for non_prime in non_primes[1:]:
        result = gcd(non_prime, result)
        
    return result

# 44
def find_five_indices(points):
    point_to_index = {point: index for index, point in enumerate(points)}
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    for x, y in points:
        for dx, dy in directions:
            line = [point_to_index[(x, y)]]
            new_x, new_y = x + dx, y + dy
            while (new_x, new_y) in point_to_index:
                line.append(point_to_index[(new_x, new_y)])
                new_x += dx
                new_y += dy
                if len(line) == 5:
                    return line
    return []

# 45
def rank(scores):
    averages = dict()
    for contestant, score in scores.items():
        averages[contestant] = round((sum(score) - max(score) - min(score)) / (len(score) - 2), 2)
    
    ranked = sorted(set(averages.values()), reverse=True)
    
    return [(ranked.index(averages[c]) + 1, c, averages[c]) for c in averages]

# 46
def avg_rating(votes):
    restaurant_to_stats = dict()
    for restaurant, vote in votes:
        if vote == "NA":
            continue
        if restaurant not in restaurant_to_stats:
            restaurant_to_stats[restaurant] = [0, 0]
        restaurant_to_stats[restaurant][0] += vote
        restaurant_to_stats[restaurant][1] += 1
    return {restaurant: (total / count) for restaurant, (total, count) in restaurant_to_stats.items()}

# 47
uni = {
    'items': [
        {'name': 'Massachusetts Institute of Technology (MIT)', 'city': 'Cambridge', 'country': 'USA'},
        {'name': 'Imperial College London', 'city': 'London', 'country': 'UK'},
        {'name': 'University of Oxford', 'city': 'Oxford', 'country': 'UK'},
        {'name': 'Harvard University', 'city': 'Cambridge', 'country': 'USA'},
        {'name': 'University of Cambridge', 'city': 'Cambridge', 'country': 'UK'}
    ],
    'overall_rank': [1, 2, 3, 4, 5],
    'cs_rank': [1, 16, 4, 7, 8],
    'mba_rank': [4, 18, 19, 3, 7]
}

def get_university_rank(choice_of_rank):
    if not choice_of_rank.endswith("_rank"):
        choice_of_rank += "_rank"
    if choice_of_rank not in uni:
        return []
    rankings = []
    for rank, item in zip(uni[choice_of_rank], uni["items"]):
        rankings.append((rank, item["name"], item["city"]))
    return rankings

# 48
def find_pattern_with_single_q(text, pat):
    pat_length = len(pat)
    for index, start in enumerate(text[:len(text) - pat_length + 1]):
        is_wildcard_used = False
        is_match = True
        for substring_index, char in enumerate(text[index:index + pat_length]):
            pat_char = pat[substring_index]
            if pat_char == "?" and not is_wildcard_used:
                is_wildcard_used = True
                continue
            if pat_char != char:
                is_match = False
                break
        if is_match:
            return index
    return -1

# 49
def find_pattern_with_star(text, pat):
    pat_sections = pat.split("*")
    search_index = 0
    first_match = 0 if pat.startswith("*") else -1
    for section in pat_sections:
        if section == "":
            continue
        section_length = len(section)
        search_area = text[search_index:]
        is_found = False
        for index, start in enumerate(search_area[:len(search_area) - (section_length) + 1]):
            if search_area[index:index + section_length] == section:
                is_found = True
                if first_match == -1:
                    first_match = index + search_index
                break
        if is_found:
            search_index += index + section_length
        else:
            return -1
    return first_match

# 50
import numpy as np

def most_similar_year_pair(temps):
    values = list(temps.items())
    lowest = float("inf")
    year_1 = 0
    year_2 = 0
    for index, (year, value) in enumerate(values[:-1]):
        for (year2, value2) in values[index + 1:]:
            print(year, year2)
            dist = np.sqrt(sum((value[i] - value2[i]) ** 2 for i in range(len(value))))
            if dist < lowest:
                print(year, year2, dist)
                lowest = dist
                year_1 = year
                year_2 = year2
    return (year_1, year_2)