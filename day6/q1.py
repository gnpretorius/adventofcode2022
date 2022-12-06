#MAIN
line = open('input.txt').read()

for i in range(len(line)): 

    if (i >= 4): #only start processing after the 4 char min
        if len(set(line[i-3] + line[i-2] + line[i-1] + line[i])) == 4:
            print(i + 1) #question is 1 based index
            break

