"""https://adventofcode.com/2025/day/5 Part 1
"""

TEST_INPUT_PATH = 'inputs/5.test.txt'
INPUT_PATH = 'inputs/5.ingredients.txt'

with open(INPUT_PATH, encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]
    fresh_ranges, ingredients = [], []
    for line in lines:
        parts = line.split('-')
        if len(parts) == 2:
            start, end = map(int, parts)
            fresh_ranges.append((start, end))
        elif parts[0]:
            ingredients.append(int(parts[0]))

    ingredients.sort()
    fresh_ranges.sort()

    no_overlap_ranges = []
    curr_start, curr_end = None, None
    for start, end in fresh_ranges:
        if curr_start is None:
            curr_start, curr_end = start, end
        elif start > curr_end:
            no_overlap_ranges.append((curr_start, curr_end))
            curr_start, curr_end = start, end
        else:
            curr_end = max(curr_end, end)
    if curr_start is not None:
        no_overlap_ranges.append((curr_start, curr_end))

    curr_range_index = 0
    fresh_ingredients = []
    for ingredient in ingredients:
        curr_start, curr_end = no_overlap_ranges[curr_range_index]
        if ingredient < curr_start:
            continue
        elif curr_start <= ingredient <= curr_end:
            fresh_ingredients.append(ingredient)
        else:
            while curr_range_index + 1 < len(no_overlap_ranges):
                curr_range_index += 1
                curr_start, curr_end = no_overlap_ranges[curr_range_index]
                if ingredient < curr_start:
                    break
                if curr_start <= ingredient <= curr_end:
                    fresh_ingredients.append(ingredient)
                    break

    print(f'Fresh ingredients: {fresh_ingredients}')
    print(f'Number of fresh ingredients: {len(fresh_ingredients)}')

    print('-' * 20)
    count_fresh_ids = 0
    for start, end in no_overlap_ranges:
        count_fresh_ids += end - start + 1
    print(f'Number of fresh ingredient IDs: {count_fresh_ids}')
