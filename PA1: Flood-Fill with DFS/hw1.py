#!/usr/bin/python
from collections import deque

# function to print input and output arrays
def print_arr(arr):
    try:
        printlist = []
        j = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                printlist += arr[i][j]
            if j != 0:   # edge case when only one row/column
                print(printlist)
            else:
                print(arr)
            printlist = []
    except IndexError:
        print(arr)


def print_answer(solution):
    total_modified = 0
    print('List of cell locations modified:')
    curr_row = 0
    for key in sorted(solution.keys()):
        x, y = key
        if x != curr_row:
            print()
            curr_row = x
        print(key, end=',')
        total_modified += 1
    print()
    print()
    print('Number of cells modified:', total_modified)


# Below lists detail all eight possible movements
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# check if it is possible to go to pixel (x, y) from the current pixel.
# The function returns false if the pixel has a different color, or it's not a valid pixel
def is_safe(mat, x, y, target):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target


def flood_fill(twodarr, start_x, start_y, target_color, replacement_color):
    print('\n Changing ', target_color, 'to', replacement_color, ' in Input Array:')
    print_arr(twodarr)
    solution = {}
    # base case: empty array
    if len(twodarr) == 0:
        print("Empty Array Case")
    # Change color of target index
    # Check if surrounding indices same color and reachable from target
    elif twodarr[start_x][start_y] == target_color:

        # create a queue and enqueue starting pixel
        q = deque()
        twodarr[start_x][start_y] = replacement_color
        solution[start_x, start_y] = 1
        q.append((start_x, start_y))

        # break when the queue becomes empty
        while q:

            # dequeue front node and process it
            x, y = q.popleft()
            solution[x, y] = 1

            # process all eight adjacent pixels of the current pixel and
            # enqueue each valid pixel
            for k in range(len(row)):
                # if the adjacent pixel at position (x + row[k], y + col[k]) is
                # is valid and has the same color as the current pixel
                if is_safe(twodarr, x + row[k], y + col[k], target_color):
                    # replace the current pixel color with that of replacement
                    twodarr[x + row[k]][y + col[k]] = replacement_color

                    # enqueue adjacent pixel
                    q.append((x + row[k], y + col[k]))

    print_answer(solution)
    print('Output Array:')
    print_arr(twodarr)


def main():
    # read in test files here then run them
    exec(open('testcase1.py').read())
    exec(open('testcase2.py').read())
    exec(open('testcase3.py').read())
    exec(open('testcase4.py').read())
    exec(open('testcase5.py').read())
    exec(open('testcase6.py').read())
    exec(open('testcase7.py').read())
    exec(open('testcase8.py').read())


if __name__ == "__main__":
    main()
