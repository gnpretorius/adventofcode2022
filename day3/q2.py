# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
    

#MAIN
lines = open('input.txt').read().splitlines()
intersects = []
total_score = 0

for i in range(0, len(lines), 3) :
    intersect = set(lines[i]).intersection(lines[i + 1])

    segment1 = ""
    while len(intersect) > 0:
        segment1 += str(intersect.pop())

    intersect = set(segment1).intersection(lines[i + 2])
    final_char = str(intersect.pop())   

    priority_score = 0

    if ord(final_char) < 97:
        priority_score = ord(final_char) - 64 + 26
    else:
        priority_score = ord(final_char) - 96

    total_score += priority_score 
    
print(total_score)