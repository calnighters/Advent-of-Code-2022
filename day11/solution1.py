from math import floor

class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.interactions = 0
    
    def interact(self):
        self.interactions += 1
    
    def has_items(self):
        return len(self.items) > 0

def calculate_worry(worry, monkey):
    operation = monkey.operation.split()
    operator = operation[-2]
    value = operation[-1]
    if value == 'old':
        value = worry
    else:
        value = int(value)
        
    if operator == '+':
        return worry + value
    else:
        return worry * value
    
def divide_worry(worry):
    return floor(worry / 3)
    
def true_test(monkey, worry):
    return (worry % monkey.test) == 0
    
def solve_part1(monkeys):
    for i in range(0, 20):
        for idx, monkey in enumerate(monkeys):
            if monkey.has_items():
                for item in monkey.items:
                    worry = int(item)
                    worry = calculate_worry(worry, monkey)
                    worry = divide_worry(worry)
                    if true_test(monkey, worry):
                        monkeys[monkey.true].items.append(worry)
                    else:
                        monkeys[monkey.false].items.append(worry)
                    monkeys[idx].interact()
                monkeys[idx].items.clear()
        
    monkeys = sorted(monkeys, key=lambda monkey: monkey.interactions)
    return monkeys[-2].interactions * monkeys[-1].interactions

monkeys = []
monkey = Monkey(None, None, None, None, None)

with open("day11/input.txt") as input_file:
# with open("test.txt") as input_file:
    for line in input_file:
        stripped_line = line.strip()
        if stripped_line == '':
            monkeys.append(monkey)
            monkey = Monkey(None, None, None, None, None)
        elif stripped_line.startswith('Starting items: '):
            monkey.items = stripped_line[16:].replace(',', '').split()
        elif stripped_line.startswith('Operation: '):
            monkey.operation = stripped_line[11:]
        elif stripped_line.startswith('Test: '):
            monkey.test = int(line.split()[-1])
        elif stripped_line.startswith('If true: '):
            monkey.true = int(line.split()[-1])
        elif stripped_line.startswith('If false: '):
            monkey.false = int(line.split()[-1])
monkeys.append(monkey)
        
print("Part 1: " + str(solve_part1(monkeys)))
