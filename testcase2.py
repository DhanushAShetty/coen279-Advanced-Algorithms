# large 8x9 array test case from Question
print("large 8x9 array test case from Question:")
testarr = [
            ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'X', 'X', 'X'],
            ['Y', 'Y', 'Y', 'Y', 'G', 'G', 'R', 'X', 'X'],
            ['Y', 'G', 'G', 'G', 'G', 'G', 'R', 'X', 'X'],
            ['Y', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['Y', 'G', 'G', 'G', 'R', 'R', 'X', 'X', 'X'],
            ['Y', 'G', 'X', 'G', 'G', 'G', 'G', 'X', 'X'],
            ['Y', 'G', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

startx = 7
starty = 8
replacment = 'g'
label = 'G'
HW1(testarr, startx, starty, label, replacment)