"""https://adventofcode.com/2025/day/1 Part 2
"""

with open('inputs/1.safe_dial_turns.txt', enconding='utf-8') as f:
    # read safe dial rotations from file (e.g.: 'L31', 'R9')
    # convert directions to signs (negative for 'L', positive for 'R')
    # convert steps to positive integers
    lines = [(-1 if x[0] == 'L' else 1, int(x[1:])) for x in f]
    # combine direction and step count to +ve/-ve integer
    turns = [x[0]*x[1] for x in lines]
    position, zeroes = 50, 0
    for turn in turns:
        div, mod = divmod(position + turn, 100)
        zeroes += abs(div)
        if turn < 0:
            if mod == 0:
                zeroes += 1
            elif position == 0:
                zeroes -= 1
        position = mod
    print(zeroes)