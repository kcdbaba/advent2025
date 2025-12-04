"""https://adventofcode.com/2025/day/3 Part 1
"""

INPUT_FILE = 'inputs/3.battery_jolts.txt'
TEST_INPUT_FILE = 'inputs/3.test.txt'
with open(INPUT_FILE, encoding='utf-8') as f:
    bank_jolts = []
    for line in f:
        battery_jolts = [int(x) for x in list(line.strip())]
        first_index = battery_jolts.index(max(battery_jolts[:-1]))
        second_index = battery_jolts.index(max(battery_jolts[first_index+1:]))
        max_joltage = battery_jolts[first_index]*10 + battery_jolts[second_index]
        bank_jolts.append(max_joltage)
    print(f'Total output joltage: {sum(bank_jolts)}')
