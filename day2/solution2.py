def determine_result_loss(opponent):
    if opponent == 'A':
        return 3
    if opponent == 'B':
        return 1
    if opponent == 'C':
        return 2
    
def determine_result_draw(opponent):
    if opponent == 'A':
        return 4
    if opponent == 'B':
        return 5
    if opponent == 'C':
        return 6
    
def determine_result_win(opponent):
    if opponent == 'A':
        return 8
    if opponent == 'B':
        return 9
    if opponent == 'C':
        return 7
    
def points(opponent, you):
    score = 0
    if you == 'X':
        score += determine_result_loss(opponent)
    elif you == 'Y':
        score += determine_result_draw(opponent)
    elif you == 'Z':
        score += determine_result_win(opponent)
    return score
        

lines = []

input_file = open("day2/input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

total = 0

for line in lines:
    total += points(line[0], line[2])

print("Part 2: " + str(total))