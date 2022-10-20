# Average array test case
from hw1 import flood_fill

test_arr = [
    ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
    ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
    ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
    ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
    ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
    ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
    ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
    ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]
start_x = 3
start_y = 9
replacement = 'C'
target = 'X'
flood_fill(test_arr, start_x, start_y, target, replacement)
