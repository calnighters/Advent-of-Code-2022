def find_answer(signals):
    total = 0
    for signal in signals:
        total += (signal[0] * signal[1])
    return total

def solve_part1(input):
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
    
    sigs = []
    while cycle < cycles_required:
        if (cycle + 1) % 40 == 20:
            print(cycle, signal_strength)
            sigs.append([cycle+1, signal_strength])
        val = vals_queue[0][0]
        req = vals_queue[0][1]
        req -= 1
        cycle += 1
        vals_queue[0][1] = req
        if req == 0:
            signal_strength += val
            vals_queue.pop(0)
    return find_answer(sigs)
    
input = []
with open("day10/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        input.append(line.strip().split())
        
print("Part 1: " + str(solve_part1(input)))
