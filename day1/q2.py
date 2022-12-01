lines = open('input.txt').read().splitlines() #avoid pending a new line to each line like other methods 
calories = []
current_calories = 0

for line in lines:
   
    if line == "":
        # reset calories 
        calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line)


calories.sort(reverse=True)

print(calories[0] + calories[1] + calories[2])