# large 8x9 array test case from Question
from hw1 import flood_fill

test_arr = [
            ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'X', 'X', 'X'],
            ['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'X', 'X'],
            ['Y', 'G', 'G', 'G', 'G', 'R', 'X', 'X', 'X'],
            ['Y', 'G', 'G', 'G', 'R', 'R', 'X', 'X', 'X'],
            ['Y', 'G', 'X', 'G', 'G', 'G', 'G', 'X', 'X'],
            ['Y', 'G', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

start_x = 7
start_y = 8
replacement = 'G'
target = 'X'
flood_fill(test_arr, start_x, start_y, target, replacement)
