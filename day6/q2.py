#MAIN
line = open('input.txt').read()

for i in range(len(line)): 

    if (i >= 14): #only start processing after the 4 char min

        message = ""
        for c in range(0,14):
            message += line[i-c]
        
        if len(set(message)) == 14:
            print(i + 1) #question is 1 based index
            break
