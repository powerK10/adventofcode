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
res = np.diff(l,1)
res = res[res[:] > 0]
final_result = res.size
print(final_result)

#initiate pandas list of values:
#list_data = pd.Series(array_raw_data.transpose())
#print(list_data)

#export AOC_SESSION=cafef00db01dfaceba5eba11deadbeef
#from aocd import data
