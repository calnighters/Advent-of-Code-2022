def determine_result_rock(opponent):
    if opponent == 'A':
        return 3
    if opponent == 'B':
        return 0
    if opponent == 'C':
        return 6
    
def determine_result_paper(opponent):
    if opponent == 'A':
        return 6
    if opponent == 'B':
        return 3
    if opponent == 'C':
        return 0
    
def determine_result_scissors(opponent):
    if opponent == 'A':
        return 0
    if opponent == 'B':
        return 6
    if opponent == 'C':
        return 3
    
def points(opponent, you):
    score = 0
    if you == 'X':
        score += 1
        score += determine_result_rock(opponent)
    elif you == 'Y':
        score += 2
        score += determine_result_paper(opponent)
    elif you == 'Z':
        score += 3
        score += determine_result_scissors(opponent)
    return score
        

lines = []

input_file = open("day2/input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

total = 0

for line in lines:
    total += points(line[0], line[2])

print("Part 1: " + str(total))