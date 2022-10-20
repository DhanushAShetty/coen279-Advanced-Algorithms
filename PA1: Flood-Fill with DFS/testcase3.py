# very large 9x10 array test case
from hw1 import flood_fill

test_arr = [
            ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'R', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'X', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'Y', 'Y', 'Y', 'G', 'G', 'R', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'G', 'G', 'G', 'G', 'G', 'R', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'G', 'G', 'G', 'R', 'R', 'X', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'G', 'X', 'G', 'G', 'G', 'G', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R'],
            ['Y', 'G', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'B', 'B', 'B',
             'R', 'R',  'R', 'R', 'R', 'R']
        ]
start_x = 8
start_y = 8
replacement = 'Y'
target = 'X'
flood_fill(test_arr, start_x, start_y, target, replacement)
