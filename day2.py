import numpy as np
import pandas as pd
import urllib
import aocd
# getting data from aoc:
from aocd import get_data
raw_data = get_data(day=2, year=2021)

# splitting data into an array
l = raw_data.splitlines()

hor_pos = 0
depth = 0
for i in l:
    if "forward" in i:
        s = list(filter(str.isdigit, i))[0]
        hor_pos += int(s)
    elif "down" in i:
        s = list(filter(str.isdigit, i))[0]
        depth += int(s)
    elif "up" in i:
        s = list(filter(str.isdigit, i))[0]
        depth -= int(s)

# getting final results
final_results_part1 = hor_pos*depth
print("Final results for day2 part1: ", final_results_part1)
