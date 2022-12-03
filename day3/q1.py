# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
    

#MAIN
lines = open('input.txt').read().splitlines()
total_score = 0

for line in lines:

    segment_length = int(len(line) / 2)
    segment1 = line[0:segment_length]
    segment2 = line[segment_length:segment_length*2]
    intersect = str(set(segment1).intersection(segment2).pop()) # validated always 1
    priority_score = 0

    if ord(intersect) < 97:
        priority_score = ord(intersect) - 64 + 26
    else:
        priority_score = ord(intersect) - 96

    total_score += priority_score
    
print(total_score)


