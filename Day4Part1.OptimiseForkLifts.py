"""https://adventofcode.com/2025/day/4 Part 1
"""

TEST_INPUT_PATH = 'inputs/4.test.txt'
INPUT_PATH = 'inputs/4.grid.txt'
with open(INPUT_PATH, encoding='utf-8') as f:
    lines = [list(line.strip()) for line in f.readlines()]
    width = len(lines[0])
    height = len(lines)
    grid = [[x=='@' for x in line] for line in lines]

    neighbor_idxs_offsets = [(i, j) for i in (-1, 0, 1) for j in [-1, 1]]
    neighbor_idxs_offsets.extend([(-1, 0), (1, 0)])
    def count_neighbouring_rolls(selfx, selfy):
        neighbour_idxs = [(selfx + x_off, selfy + y_off) for x_off, y_off in neighbor_idxs_offsets
                          if 0 <= selfx + x_off < width and 0 <= selfy + y_off < height]
        neighbour_count = sum(grid[x][y] for (x,y) in neighbour_idxs)
        return neighbour_count

    def remove_all_accessible_rolls():
        cnt = 0
        accessible_coords = []
        for x in range(width):
            for y in range(height):
                if grid[x][y] and count_neighbouring_rolls(x, y) < 4:
                    lines[x][y] = 'x'
                    accessible_coords.append((x,y))
                    cnt += 1
        #for line in lines:
        #    print(''.join(line))
        for (x, y) in accessible_coords:
            grid[x][y] = False
        return cnt

count = remove_all_accessible_rolls()
print(f'Rolls of paper to be removed after round 1: {count} ')
rounds = 1
more_count = count
while more_count > 0:
    more_count = remove_all_accessible_rolls()
    rounds += 1
    print(f'Rolls of paper to be removed after round {rounds}: {more_count} ')
    count += more_count
print(f'Total rolls of paper to be removed: {count} ')
