def create_location(x, y):
    return str(x) + ',' + str(y)

def workout_tail(tail_x, tail_y, head_x, head_y):
    if tail_x == head_x:
        diff = head_y - tail_y
        if diff == 2:
            return [tail_x, tail_y + 1]
        elif diff == -2:
            return [tail_x, tail_y - 1]
        else:
            return [tail_x, tail_y]
    elif tail_y == head_y:
        diff = head_x - tail_x
        if diff == 2:
            return [tail_x + 1, tail_y]
        elif diff == -2:
            return [tail_x - 1, tail_y]
        else:
            return [tail_x, tail_y]
    elif abs(head_y - tail_y) != 0 and abs(head_x - tail_x) != 0:
        diff_x = head_x - tail_x
        diff_y = head_y - tail_y
        if abs(diff_x) == 1 and abs(diff_y) == 1:
            return [tail_x, tail_y]
        if diff_x > 0 and diff_y > 0:
            return [tail_x + 1, tail_y + 1]
        elif diff_x > 0 and diff_y < 0:
            return [tail_x + 1, tail_y - 1]
        elif diff_x < 0 and diff_y > 0:
            return [tail_x - 1, tail_y + 1]
        else:
            return [tail_x - 1, tail_y - 1]
    else:
        return [tail_x, tail_y]

def workout_tails(tails, head_x, head_y):
    new_tails = tails
    for i in range(0, len(new_tails)):
        if i == 0:
            new_tails[i] = workout_tail(new_tails[i][0], new_tails[i][1], head_x, head_y)
        else:
            new_tails[i] = workout_tail(new_tails[i][0], new_tails[i][1], new_tails[i-1][0], new_tails[i-1][1])
    return new_tails
    
def move(command, tails, head_x, head_y):
    new_head_x = head_x
    new_head_y = head_y
    new_tails = tails
    locations = []
    for i in range(0, int(command[1])):
        if command[0] == 'U':
            new_head_y += 1
        if command[0] == 'D':
            new_head_y -= 1
        if command[0] == 'L':
            new_head_x -= 1
        if command[0] == 'R':
            new_head_x += 1
        new_tails = workout_tails(new_tails, new_head_x, new_head_y)
        new_tail_x = new_tails[-1][0]
        new_tail_y = new_tails[-1][1]
        locations.append(create_location(new_tail_x, new_tail_y))
    return [new_tails, new_head_x, new_head_y, locations]

def solve(input):
    tails = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    head_x = 0
    head_y = 0
    locations = ['0,0']
    for command in input:
        movement = move(command, tails, head_x, head_y)
        tails = movement[0]
        head_x = movement[1]
        head_y = movement[2]
        locations.extend(movement[3])
    return len(set(locations))
    
input=[]
with open("day9/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        split = line.strip().split()
        input.append([split[0], split[1]])
        
print("Part 2: " + str(solve(input)))
