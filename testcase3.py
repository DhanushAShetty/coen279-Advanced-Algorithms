# very large 9x10 array test case
print("very large 9x10 array test case:")
testarr = [
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
startx = 8
starty = 8
replacment = 'Y'
label = 'X'
HW1(testarr, startx, starty, label, replacment)
