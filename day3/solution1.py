def get_char_val(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return (ord(char)-38)
    return (ord(char)-96)

def find_total(line):
    matches = []
    total = 0
    compartment_1 = line[:len(line)//2]
    compartment_2 = line[len(line)//2:]
    print(line + " " + compartment_1 + " " + compartment_2)
    for a in compartment_1:
        for b in compartment_2:
            if a == b and not matches.__contains__(a):
                matches.append(a)
                char_val = get_char_val(a)
                print(a + " " + str(char_val))
                total += char_val
    return total
    
lines = []

input_file = open("day3/input.txt", "r")
# input_file = open("test.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

total = 0

for line in lines:
    total += find_total(line)

print("Part 1: " + str(total))