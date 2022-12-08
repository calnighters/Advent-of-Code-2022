def find_up(x_coord, y_coord, trees):
    in_line = []
    for i in range(y_coord - 1, -1, -1):
        in_line.append(trees[i][x_coord])
    return in_line

def find_left(x_coord, y_coord, trees):
    in_line = []
    for i in range(x_coord - 1, -1, -1):
        in_line.append(trees[y_coord][i])
    return in_line

def find_right(x_coord, y_coord, trees):
    in_line = []
    right_limit = len(trees[0])
    for i in range(x_coord + 1, right_limit):
        in_line.append(trees[y_coord][i])
    return in_line

def find_down(x_coord, y_coord, trees):
    in_line = []
    bottom_limit = len(trees)
    for i in range(y_coord + 1, bottom_limit):
        in_line.append(trees[i][x_coord])
    return in_line

def is_visible(up, down, left, right, height):
    up.sort()
    down.sort()
    left.sort()
    right.sort()
    
    visible_up = True
    for tree in up:
        if int(tree) >= int(height):
            visible_up = False
            break
    
    visible_down = True
    for tree in down:
        if int(tree) >= int(height):
            visible_down = False
            break
        
    visible_right = True
    for tree in right:
        if int(tree) >= int(height):
            visible_right = False
            break
        
    visible_left = True
    for tree in left:
        if int(tree) >= int(height):
            visible_left = False
            break
        
    return visible_up or visible_down or visible_left or visible_right
    
def find_scenic_score(up, down, left, right, height):
    scores = []
    
    up_count = 0
    for tree in up:
        up_count += 1
        if int(tree) >= int(height):
            break
    scores.append(up_count)
    
    down_count = 0
    for tree in down:
        down_count += 1
        if int(tree) >= int(height):
            break
    scores.append(down_count)
    
    left_count = 0
    for tree in left:
        left_count += 1
        if int(tree) >= int(height):
            break
    scores.append(left_count)
    
    right_count = 0
    for tree in right:
        right_count += 1
        if int(tree) >= int(height):
            break
    scores.append(right_count)
    
    return scores[0] * scores[1] * scores[2] * scores[3]
    
def solve_part1(trees):
    visible_trees = 0
    for oidx, oval in enumerate(trees):
        for iidx, ival in enumerate(oval):
            up = find_up(iidx, oidx, trees)
            down = find_down(iidx, oidx, trees)
            left = find_left(iidx, oidx, trees)
            right = find_right(iidx, oidx, trees)
            if is_visible(up, down, left, right, ival):
                visible_trees += 1
    return visible_trees

def solve_part2(trees):
    max_scenic_score = 0
    for oidx, oval in enumerate(trees):
        for iidx, ival in enumerate(oval):
            up = find_up(iidx, oidx, trees)
            down = find_down(iidx, oidx, trees)
            left = find_left(iidx, oidx, trees)
            right = find_right(iidx, oidx, trees)
            score = find_scenic_score(up, down, left, right, ival)
            if score > max_scenic_score:
                max_scenic_score = score
    return max_scenic_score
    
grid = []
with open("day8/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        grid.append(list(line.strip()))
        
print("Part 1: " + str(solve_part1(grid)))
print("Part 2: " + str(solve_part2(grid)))
