from collections import defaultdict
from statistics import mode

FILENAME = "input"

d = defaultdict(list)

with open(FILENAME) as f:
    for line in f:
        for index, char in enumerate(line.rstrip()):
            d[index].append(char)

    gamma_binary_string = ''.join([mode(d[key]) for key in d.keys()])
    epsilon_binary_string = ''.join('1' if x == '0' else '0' for x in gamma_binary_string)

    gamma_int = int(gamma_binary_string, 2)
    epsilon_int = int(epsilon_binary_string, 2)

    power_consumption = gamma_int * epsilon_int

    print(power_consumption)