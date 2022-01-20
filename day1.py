import numpy as np
import pandas as pd
import urllib
import aocd
# getting data from aoc:
from aocd import get_data
raw_data = get_data(day=1, year=2021)

# splitting data into an array
l = raw_data.splitlines()

#converting to numbers:
l = [int(n) for n in l]

#using numpy diff function to get
#difference between one value and previous value
res = np.diff(l,1)

#finding out all increases:
res = res[res[:] > 0]

# getting final result by simply getting
# size of this 1d array:
final_result_part1 = res.size
print("Results for day1 part 1: " + str(final_result_part1))

# Part 2
loop_count = 0
sum3_array = [0] * (len(l)-2) #np.zeros(len(l)-2)
for i in l:
    sum3 = l[loop_count] + l[loop_count+1] + l[loop_count+2]
    sum3_array[loop_count] = sum3
    loop_count += 1
    #break the sums at the end
    if loop_count == len(l)-2:
        break

#similarly as in part 1, finding increases:
res_sum3 = np.diff(sum3_array,1)
res_sum3 = res_sum3[res_sum3[:] > 0]
final_result_part2 = res_sum3.size
print("results for day1 part 2: " + str(final_result_part2))
