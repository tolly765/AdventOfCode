input = open("input.txt", "r")
sonarLines = input.readlines()

task1Count = 1 # First line is always bigger than 0
lineCount = len(sonarLines)

i = 0
while i <= lineCount:
    try:
        comp1 = sonarLines[i]
        comp2 = sonarLines[i+1]
        if comp2 > comp1:
            task1Count = task1Count + 1
    except IndexError:
        print(f"Total greater than previous: {task1Count}")
    i += 1
