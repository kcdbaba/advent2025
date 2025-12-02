"""https://adventofcode.com/2025/day/1 Part 1
"""

from itertools import accumulate

with open('inputs/1.safe_dial_turns.txt', enconding='utf-8') as f:
    # read safe dial rotations from file (e.g.: 'L31', 'R9')
    # convert directions to signs (negative for 'L', positive for 'R')
    # convert steps to positive integers
    lines = [(-1 if x[0] == 'L' else 1, int(x[1:])) for x in f]
    # combine direction and step count to +ve/-ve integer
    turns = [x[0]*x[1] for x in lines]
    # starting at 50, track all positions of the safe dial (0 to 99)
    dials = list(accumulate(turns, lambda a, b : (a+b)%100, initial=50))
    # print number of time dial is at zero
    print(dials.count(0))