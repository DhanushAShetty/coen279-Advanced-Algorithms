# one column and one row array test case
from hw1 import flood_fill

test_arr = [['B'], ['R']]

start_x = 0
start_y = 0
replacement = 'W'
target = 'B'
flood_fill(test_arr, start_x, start_y, target, replacement)
