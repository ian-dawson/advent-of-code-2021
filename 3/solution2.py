from collections import defaultdict
import operator

FILENAME = "input"

def filter(binary_strings, op, position):
    common = '1' if op([x[position] for x in binary_strings].count('1'), len(binary_strings)/2) else '0'
    filtered_list = [x for x in binary_strings if x[position] == common]
    if len(filtered_list) != 1:
        return filter(filtered_list, op, position + 1)
    else:
        return filtered_list
        
with open(FILENAME) as f:
    starting_list = f.read().splitlines()

    oxygen_generator_rating_string = ''.join(filter(starting_list, operator.ge, 0))
    co2_scrubber_rating_string = ''.join(filter(starting_list, operator.lt, 0))

    oxygen_generator_rating = int(oxygen_generator_rating_string, 2)
    o2_scrubber_rating = int(co2_scrubber_rating_string, 2)

    life_support_rating = oxygen_generator_rating*o2_scrubber_rating

    print(life_support_rating)