# 2 pairs split by comma 
# each pair, two number separated by dash 
    
counter = 0
total = 0

#MAIN
lines = open('input.txt').read().splitlines()

for line in lines:

    pair1num1 = int(line.split(",")[0].split("-")[0])
    pair1num2 = int(line.split(",")[0].split("-")[1])

    pair2num1 = int(line.split(",")[1].split("-")[0])
    pair2num2 = int(line.split(",")[1].split("-")[1])

    if pair1num1 <= pair2num1 and pair1num2 >= pair2num2:
        counter += 1
    
    elif pair2num1 <= pair1num1 and pair2num2 >= pair1num2:
        counter += 1

    total += 1


print(counter, total)


