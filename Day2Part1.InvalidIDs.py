"""https://adventofcode.com/2025/day/2 Part 1
"""

def twice_repeat_ids(min_id, max_id, prev_seq=''):
    min_id_int = int(min_id)
    max_id_int = int(max_id)
    #print(f'Checking range {min_id} to {max_id} with prev_seq {prev_seq}')
    twice_repeats = []
    if prev_seq == '' and len(min_id) < len(max_id):
        twice_repeats += twice_repeat_ids(min_id, '9'*len(min_id))
        for length in range(len(min_id)+1, len(max_id)):
            twice_repeats += twice_repeat_ids('1'+'0'*(length-1), '9'*length)
        twice_repeats += twice_repeat_ids('1' + '0'*(len(max_id)-1), max_id)
        return twice_repeats

    if (len(prev_seq) + len(max_id)) % 2 != 0:
        #print(f'Odd length for {prev_seq+min_id} and {prev_seq+max_id}, returning []')
        return []

    min_first_half = min_id[:len(min_id)//2]
    max_first_half = max_id[:len(max_id)//2]
    for pat in range(int(min_first_half), int(max_first_half)+1):
        candidate = int(str(pat)*2)
        if candidate >= min_id_int and candidate <= max_id_int:
            twice_repeats.append(candidate)
    return twice_repeats


INPUT_FILE = 'inputs/2.invalid_ids.txt'
TEST_INPUT_FILE = 'inputs/2.test.txt'
with open(INPUT_FILE, encoding='utf-8') as f:
    id_ranges = f.read().split(',')
    id_ranges = [x.split('-') for x in id_ranges]
    id_ranges = [(x[0], x[1]) for x in id_ranges]
    all_invalid_ids = []
    for (min_id, max_id) in id_ranges:
        invalid_ids = twice_repeat_ids(min_id, max_id)
        if invalid_ids:
            print(f'Invalid IDs between {min_id} and {max_id}: {invalid_ids}')
        else:
            print(f'No invalid IDs between {min_id} and {max_id}')
        all_invalid_ids += invalid_ids
    print('--------------------------------------------------------')
    print(f'Total sum of invalid IDs: {sum(all_invalid_ids)}')
