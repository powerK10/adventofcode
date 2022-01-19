import numpy as np
import pandas as pd

import urllib

import requests
import os
link = "https://adventofcode.com/2021/day/1/input"
f = requests.get(link)
#print(f.text)
print(os.environ)
import aocd

#aocd.cookies.scrape_session_tokens()
#print(aocd(scrape_session_tokens))
#
from aocd import data
from aocd import get_data
y = get_data(day=1, year=2021)
print(y)

#export AOC_SESSION=cafef00db01dfaceba5eba11deadbeef
#from aocd import data
