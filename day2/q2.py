def calculate_score(outcome, opponent):
    
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won

    if outcome == "X": # lose
        if opponent == "A": return 0 + 3 
        if opponent == "B": return 0 + 1
        if opponent == "C": return 0 + 2

    if outcome == "Y": # draw
        if opponent == "A": return 3 + 1
        if opponent == "B": return 3 + 2 
        if opponent == "C": return 3 + 3

    if outcome == "Z": # win
        if opponent == "A": return 6 + 2
        if opponent == "B": return 6 + 3
        if opponent == "C": return 6 + 1
     
#MAIN
lines = open('input.txt').read().splitlines()
total_score = 0

for line in lines:
    parts = line.split()
    total_score += calculate_score(parts[1], parts[0])


print(total_score)
   




