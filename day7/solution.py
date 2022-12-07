size_total = 0

def find_index(dir, directories):
    for i in range(0, len(directories)):
        if directories[i][0] == dir:
            return i
    return None
    
def process_input(input):
    directories = []
    directory_trail = []
    current_dir = ''
    for line in input:
        split_input = line.split(' ')
        if line[0] == '$':
            if split_input[1] == 'cd':
                if split_input[2] == '..':
                    popped_dir = current_dir
                    directory_trail.pop()
                    current_dir = directory_trail[-1]
                    directories[find_index(current_dir, directories)][1] += directories[find_index(popped_dir, directories)][1]
                else:
                    if current_dir != '/':
                        dir = split_input[2]
                        if dir == '/':
                            current_dir = '/'
                        else:    
                            current_dir += ('/' + dir)
                    else:
                        current_dir += split_input[2]
                    directory_trail.append(current_dir)
                    directories.append([current_dir, 0])
        elif split_input[0].isnumeric():
            directories[find_index(current_dir, directories)][1] += int(split_input[0])
            
    higher_level = None
    for dir in reversed(directory_trail):
        if higher_level != None:
            directories[find_index(dir, directories)][1] += higher_level
        higher_level = directories[find_index(dir, directories)][1]
        
    return directories
    
def solve_part1(directories):
    total_under = 0
    for dir in directories:
        if int(dir[1]) <= 100000:
            total_under += int(dir[1])
    return total_under

def solve_part2(directories):
    directories.sort(key=lambda dir:dir[1])
    amount_needed = 30000000 - (70000000 - directories[-1][1])
    for dir in directories:
        if dir[1] >= amount_needed:
            return dir[1]

lines = []

with open("day7/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        lines.append(line.strip())
        
directories = process_input(lines)
print("Part 1: " + str(solve_part1(directories)))
print("Part 2: " + str(solve_part2(directories)))
