containers = [
    ['R', 'S', 'L', 'F', 'Q'],
    ['N', 'Z', 'Q', 'G', 'P', 'T'],
    ['S', 'M', 'Q', 'B'],
    ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'],
    ['P', 'H', 'M', 'B', 'N', 'F', 'S'], 
    ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'], 
    ['W', 'C', 'F'], 
    ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'], 
    ['G', 'Z', 'D', 'L', 'C', 'N', 'R']
    ]
# containers = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

lines = []

input_file = open("day5/input.txt", "r")
# input_file = open("test.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

def parse_line_input(line):
    arr = line.split(' ')
    return [int(arr[1]), int(arr[3]) - 1, int(arr[5]) - 1]

def find_containers(stack, amount):
    start = len(stack) - amount
    arr = []
    for i in range(start, len(stack)):
        arr.append(stack[i])
    return arr
    
def move_container(input):
    amount = input[0]
    from_stack = input[1]
    to_stack = input[2]
    
    local_containers = find_containers(containers[from_stack], amount)
    for container in local_containers:
        containers[from_stack].pop()
        containers[to_stack].append(container)

for line in lines:
    move_container(parse_line_input(line))

def print_result(arr):
    final = ''
    for stack in arr:
        final += stack[len(stack) - 1]
    return final

print("Part 2: " + print_result(containers))
