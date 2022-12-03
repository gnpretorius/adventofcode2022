def map_value_to_score(val):
    if val == "X": return 1
    if val == "Y": return 2
    if val == "Z": return 3

def play_roshambo(you, opponent):
    if you == "X" and opponent == "A": return 3 #draw
    if you == "Y" and opponent == "B": return 3 #draw
    if you == "Z" and opponent == "C": return 3 #draw

    if you == "X" and opponent == "C": return 6 #win
    if you == "Y" and opponent == "A": return 6 #win
    if you == "Z" and opponent == "B": return 6 #win

    if you == "X" and opponent == "B": return 0 #lost
    if you == "Y" and opponent == "C": return 0 #lost
    if you == "Z" and opponent == "A": return 0 #lost

#MAIN
lines = open('input.txt').read().splitlines()
total_score = 0

for line in lines:

    parts = line.split()
    
    game_score = play_roshambo(parts[1], parts[0])
    hand_score = map_value_to_score(parts[1])
    total_score += (game_score + hand_score)


print(total_score)
   




