#!/usr/bin/python
def printaarr(a):
    for i in a:
        print(i)


def HW1(twodarr, startx, starty, targetcolor, replacmentcolor):
    print("input array:")
    printaarr(twodarr)
    # base case: empty array
    if (len(twodarr) == 0):
        return
    # edge case: target color same as replacment color
    elif(twodarr[startx:starty] == replacmentcolor):
        return
    else:
        # Change color of target index
        # Check if surrounding indices same color and reachable from target
        print("outputarray:")
        printaarr(twodarr)

def main():
    # read in test files here then run them
    exec(open('testcase1.py').read())
    exec(open('testcase2.py').read())
    exec(open('testcase3.py').read())
    exec(open('testcase4.py').read())
    exec(open('testcase5.py').read())

if __name__ == "__main__":
    main()
