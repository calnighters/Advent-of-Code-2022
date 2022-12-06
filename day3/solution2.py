def get_char_val(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return (ord(char)-38)
    return (ord(char)-96)

def pop_array():
    arr = []
    for i in range(52):
        arr.append(0)
    return arr

def find_index(char):
    return get_char_val(char) - 1

def find_val_from_num(index):
    if index >= 1 and index <= 26:
        return chr(index + 96)
    return chr(index + 38)

def find_total(elves):
    matches = pop_array()
    for elf in elves:
        elf_matches = []
        for char in elf:
            if not elf_matches.__contains__(char):
                matches[find_index(char)] += 1
                elf_matches.append(char)
    for i in range(len(matches)):
        if matches[i] == 3:
            return get_char_val(find_val_from_num(i + 1))
    
lines = []

input_file = open("day3/input.txt", "r")
# input_file = open("test.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

total = 0
elves = []
elf_count = 0
for line in lines:
    elves.append(line)
    elf_count += 1
    if elf_count == 3:
        total += find_total(elves)
        elves = []
        elf_count = 0

print("Part 2: " + str(total))