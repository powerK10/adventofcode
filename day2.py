import numpy as np
import pandas as pd
import urllib
import aocd

def extract_number_from_str(i):
  f_result = int(list(filter(str.isdigit, i))[0])
  return f_result

# getting data from aoc:
from aocd import get_data
raw_data = get_data(day=2, year=2021)

# splitting data into an array
l = raw_data.splitlines()

hor_pos = 0
depth = 0
for i in l:
    s = extract_number_from_str(i)
    if "forward" in i:
        hor_pos += int(s)
    elif "down" in i:
        depth += int(s)
    elif "up" in i:
        depth -= int(s)
    else:
        raise ValueError("there is an error with input data")

# getting final results
final_results_part1 = hor_pos*depth
print("Final results for day2 part1: ", final_results_part1)

hor_pos = 0
depth = 0
aim = 0
for i in l:
    s = extract_number_from_str(i)

    if "forward" in i:
        hor_pos += s
        depth += aim*s
    elif "down" in i:
        #depth += s
        aim += s
    elif "up" in i:
        #depth -= s
        aim -= s
    else:
        raise ValueError("there is an error with input data")
# getting final results
final_results_part2 = hor_pos*depth
print("Final results for day2 part2: ", final_results_part2)
