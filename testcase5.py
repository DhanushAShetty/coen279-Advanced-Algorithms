# large simple array test case
from hw1 import flood_fill

test_arr = [
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
        ]

start_x = 1
start_y = 1
replacement = 'B'
target = 'G'
flood_fill(test_arr, start_x, start_y, target, replacement)
