lines = open('input.txt').read().splitlines() #avoid pending a new line to each line like other methods 
highest_calories  = 0
current_calories = 0

for line in lines:
   
    if line == "":
        # reset calories 
        current_calories = 0
    else:
        calories = int(line)
        current_calories += calories

        if current_calories > highest_calories:
            highest_calories = current_calories


print(highest_calories)