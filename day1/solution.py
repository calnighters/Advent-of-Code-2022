lines = []

input_file = open("day1/input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

totals = []
total = 0

for line in lines:
    if line != "":
        total += int(line)
    else:
        totals.append(total)
        total = 0
        
biggest = -1
for total in totals:
    if total > biggest:
        biggest = total
        
print("Part 1: " + str(biggest))

totals.sort(reverse=True)

print("Part 2: " + str(totals[0] + totals[1] + totals[2]))