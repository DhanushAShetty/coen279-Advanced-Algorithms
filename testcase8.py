# single columb and one row array test case
from hw1 import flood_fill

test_arr = [['G', 'G', 'G', 'G']]

start_x = 0
start_y = 0
replacement = 'W'
target = 'G'
flood_fill(test_arr, start_x, start_y, target, replacement)
