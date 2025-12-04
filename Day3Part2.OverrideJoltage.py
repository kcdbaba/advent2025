"""https://adventofcode.com/2025/day/3 Part 2
"""

INPUT_FILE = 'inputs/3.battery_jolts.txt'
TEST_INPUT_FILE = 'inputs/3.test.txt'
with open(INPUT_FILE, encoding='utf-8') as f:
    bank_jolts = []
    for line in f:
        battery_jolts = [int(x) for x in list(line.strip())]
        indices = []
        for remaining in range(12, 0, -1):
            search_start_idx = indices[-1] + 1 if indices else 0
            next_digit = max(battery_jolts[search_start_idx : (1-remaining) or None])
            index = battery_jolts.index(next_digit, search_start_idx)
            indices.append(index)
        indices.reverse()
        max_joltage = sum([battery_jolts[idx]*10**place for place, idx in enumerate(indices)])
        #print(f'Max joltage from bank {battery_jolts} is {max_joltage}')
        bank_jolts.append(max_joltage)
    print(f'Total output joltage: {sum(bank_jolts)}')
