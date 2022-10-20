# simple array test case
from hw1 import flood_fill

test_arr = [
            ['G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G'],
            ['Y', 'G', 'G', 'G'],
            ['R', 'G', 'G', 'G']
        ]
start_x = 1
start_y = 1
target = 'G'
replacement = 'B'
flood_fill(test_arr, start_x, start_y, target, replacement)
