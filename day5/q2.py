"""
        [C] [B] [H]                
[W]     [D] [J] [Q] [B]            
[P] [F] [Z] [F] [B] [L]            
[G] [Z] [N] [P] [J] [S] [V]        
[Z] [C] [H] [Z] [G] [T] [Z]     [C]
[V] [B] [M] [M] [C] [Q] [C] [G] [H]
[S] [V] [L] [D] [F] [F] [G] [L] [F]
[B] [J] [V] [L] [V] [G] [L] [N] [J]
 1   2   3   4   5   6   7   8   9 
"""

stacks = []
stacks.append(["B", "S", "V", "Z", "G", "P", "W"])
stacks.append(["J", "V", "B", "C", "Z", "F"])
stacks.append(["V", "L", "M", "H", "N", "Z", "D", "C"])
stacks.append(["L", "D", "M", "Z", "P", "F", "J", "B"])
stacks.append(["V", "F", "C", "G", "J", "B", "Q", "H"])
stacks.append(["G", "F", "Q", "T", "S", "L", "B"])
stacks.append(["L", "G", "C", "Z", "V"])
stacks.append(["N", "L", "G"])
stacks.append(["J", "F", "H", "C"])


#MAIN
lines = open('input.txt').read().splitlines()

for line in lines:

    parts = line.split()

    move_count = int(parts[1])
    from_index = int(parts[3]) - 1 # zero based index 
    to_index = int(parts[5]) - 1 # zero based index

    move_crates = []
    for i in range(move_count): 
        move_crates.append(stacks[from_index][-1])
        stacks[from_index].pop()
    
    move_crates.reverse()

    for i in move_crates:
        stacks[to_index].append(i)
    
for i in range(len(stacks)):
    print(stacks[i][-1])


