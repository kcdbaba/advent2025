"""https://adventofcode.com/2025/day/6 Part 1
"""

import operator
ops = { "+": operator.add, "*": operator.mul }
iden = { "+": 0, "*": 1 }

INPUT_PATH = 'inputs/6.cephalopod_sums.txt'
TEST_INPUT_PATH = 'inputs/6.test.txt'
with open(INPUT_PATH, encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]
    operators = lines[-1].split()
    operands = [[int(x) for x in line.split()] for line in lines[:-1]]
    total = 0
    for idx, op in enumerate(operators):
        result = iden[op]
        for row in operands:
            result = ops[op](result, row[idx])
        total += result
    print(total)
