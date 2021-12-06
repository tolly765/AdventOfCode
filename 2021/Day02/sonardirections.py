input = open("input.txt", "r")
sonarLines = input.read().splitlines()
# sonarLines = list(map(int, sonarLines))

task1Count = 0
lineCount = len(sonarLines) 
depth = 0
horiz = 0

# Task 1
i = 0
while i < lineCount:
    try:
        splitLine = sonarLines[i].split()
        if 'forward' in splitLine[0]:
            horiz = horiz + int(splitLine[1])
        elif 'up' in splitLine[0]:
            depth = depth - int(splitLine[1])

        elif 'down' in splitLine[0]:
            depth = depth + int(splitLine[1])
        else:
            pass
    except Exception as err:
        print(err)
        
    i = i + 1
print(f'Task 1: \n Horiz: {horiz} \n Depth: {depth} \n Multiplied: {horiz * depth} \n\n')

# Task 2
depth = 0
horiz = 0
aim = 0

i = 0

while i < lineCount:
    try:
        splitLine = sonarLines[i].split()
        if 'forward' in splitLine[0]:
            horiz = horiz + int(splitLine[1])
            depth = depth + (aim * int(splitLine[1]))
        elif 'up' in splitLine[0]:
            aim = aim - int(splitLine[1])
        elif 'down' in splitLine[0]:
            aim = aim + int(splitLine[1])
        else:
            pass
    except Exception as err:
        print(err)
    i = i + 1
print(f'Task 2: \n  Horiz: {horiz} \n Depth: {depth} \n Multiplied: {horiz * depth}')