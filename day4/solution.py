lines = []

input_file = open("day4/input.txt", "r")
# input_file = open("test.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

def pop_arr(min, max):
    arr = []
    for i in range(int(min), int(max) + 1):
        arr.append(i)
    return arr
    
def fully_intersects(line):
    elves = line.split(',')
    elf1_min = elves[0].split('-')[0]
    elf1_max = elves[0].split('-')[1]
    elf2_min = elves[1].split('-')[0]
    elf2_max = elves[1].split('-')[1]
    elf1 = pop_arr(elf1_min, elf1_max)
    elf2 = pop_arr(elf2_min, elf2_max)
    
    intersections_count = 0
    
    for val in elf1:
        for check in elf2:
            if val == check:
                intersections_count += 1
    return intersections_count == len(elf1) or intersections_count == len(elf2)

def intersects(line):
    elves = line.split(',')
    elf1_min = elves[0].split('-')[0]
    elf1_max = elves[0].split('-')[1]
    elf2_min = elves[1].split('-')[0]
    elf2_max = elves[1].split('-')[1]
    elf1 = pop_arr(elf1_min, elf1_max)
    elf2 = pop_arr(elf2_min, elf2_max)
    
    intersections_count = 0
    
    for val in elf1:
        for check in elf2:
            if val == check:
                intersections_count += 1
    return intersections_count > 0

full = 0
partial = 0
    
for line in lines:
    if fully_intersects(line):
        full += 1
    if intersects(line):
        partial += 1

print("Part 1: " + str(full))
print("Part 2: " + str(partial))