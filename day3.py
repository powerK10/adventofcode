import numpy as np
import pandas as pd
import urllib
import aocd
import support
import time


def day3_part1(input):
    print(type(input))
    count = len(input) # number of entries
    input_len = len(input[0])
    # initiating array where summed values will be held:
    summed_values = [0] * (input_len)
    print(input_len)
    #ignoring situation when there
    #is the same count of 0 and 1
    print("count[0]", count)
    for i in input:
        #print(i)
        for_count = 0
        for n in i:
            #print(i[for_count])
            summed_values[for_count] += int(i[for_count])
            for_count += 1

    result_array_gamma = [0] * (input_len)
    result_array_eps = [0] * (input_len)

    for_count = 0
    for u in summed_values:
        #print(u)
        if u > count/2:
            result_array_gamma[for_count] = 1
            result_array_eps[for_count] = 0
        else:
            result_array_gamma[for_count] = 0
            result_array_eps[for_count] = 1
        for_count += 1

    gamma_binary = support.get__number_from_list(result_array_gamma)
    eps_binary = support.get__number_from_list(result_array_eps)
    print(result_array_gamma)
    print(gamma_binary)

    gamma = int(str(gamma_binary),2)
    eps = int(str(eps_binary),2)

    power = gamma * eps
    print("results for day3 part1:")
    return power






test_input ="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

l = test_input.strip().splitlines()
print(l)

# expected_output = 198
# actual_output = day3_part1(l)
# time.sleep(0.5)
# assert expected_output == actual_output


# getting data from aoc:
from aocd import get_data
raw_data = get_data(day=3, year=2021)

# splitting data into an array
l = raw_data.splitlines()

print("joooo")
results_day3_part1 = day3_part1(l)
print(results_day3_part1)
