from collections import deque

HEIGHT_MAP = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}

POSSIBLE_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_start_position(grid):
    for idx, line in enumerate(grid):
        for col_idx, c in enumerate(line):
            if c == "S":
                return (idx, col_idx)


def can_move(grid, dest_row_idx, dest_col_idx, current_value):
    if (dest_row_idx < 0 or dest_col_idx < 0 or dest_row_idx >= len(grid) or dest_col_idx >= len(grid[0])):
        return False

    if current_value == "S":
        current_value = "a"

    dest_value = grid[dest_row_idx][dest_col_idx]

    if dest_value == "E":
        dest_value = "z"

    return HEIGHT_MAP[dest_value] <= HEIGHT_MAP[current_value] + 1


def find_all_low_positions(grid):
    for row_idx, l in enumerate(grid):
        for col_idx, c in enumerate(l):
            if c == "S" or c == "a":
                yield (row_idx, col_idx)


def find_shortest_path(grid, start_positions):
    queue = deque((p, 0) for p in start_positions)
    seen = set(start_positions)

    while queue:
        (current_row, current_col), current_step_count = queue.popleft()

        current_value = grid[current_row][current_col]

        if current_value == "E":
            return current_step_count

        for offset_row, offset_col in POSSIBLE_MOVES:
            new_coord = (current_row + offset_row, current_col + offset_col)

            if new_coord not in seen and can_move(grid, new_coord[0], new_coord[1], current_value):
                seen.add(new_coord)
                queue.append((new_coord, current_step_count + 1))
    return None


def solve_part1(grid):
    start_positions = [find_start_position(grid)]
    return find_shortest_path(grid, start_positions)

def solve_part2(grid):
    start_positions = list(find_all_low_positions(grid))
    return find_shortest_path(grid, start_positions)

lines = []
with open("day12/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        lines.append(line.strip())
        
print("Part 1: " + str(solve_part1(lines)))
print("Part 2: " + str(solve_part2(lines)))
