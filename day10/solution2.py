def find_answer(signals):
    total = 0
    for signal in signals:
        total += (signal[0] * signal[1])
    return total

def pixel_present(line_index, pixel):
    return (line_index >= (pixel - 1)) and (line_index <= (pixel + 1))

def solve_part2(input):
    cycle = 0
    cycles_required = 0
    vals_queue = []
    signal_strength = 1
    for command in input:
        if command[0] == 'noop':
            vals_queue.append([0, 1])
            cycles_required += 1
        else:
            vals_queue.append([int(command[1]), 2])
            cycles_required += 2
    
    lines = []
    current_line = ''
    line_index = 0
    while cycle < cycles_required:
        if cycle % 40 == 0 and cycle != 0:
            lines.append(current_line)
            current_line = ''
            line_index = 0
            
        val = vals_queue[0][0]
        req = vals_queue[0][1]
        req -= 1
        cycle += 1
        vals_queue[0][1] = req
        
        if pixel_present(line_index, signal_strength):
            current_line += "#"
        else:
            current_line += "."
        line_index += 1
        
        if req == 0:
            signal_strength += val
            vals_queue.pop(0)
    lines.append(current_line)
    return lines
    
def print_lines(lines):
    for line in lines:
        print(line)
    
input = []
with open("day10/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        input.append(line.strip().split())
        
print("Part 2: ")
print_lines(solve_part2(input))
