input = open("input.txt", "r")
sonarLines = input.read().splitlines()
sonarLines = list(map(int, sonarLines))

task1Count = 0
lineCount = len(sonarLines)

# Task 1
i = 0
while i <= lineCount:
    try:
        comp1 = sonarLines[i]
        comp2 = sonarLines[i+1]
        if comp2 > comp1:
            task1Count = task1Count + 1
    except IndexError:
        print(f"Total greater than previous: {task1Count}")
        break
    i += 1

#Task 2
i = 0
task2Count = 0
currentSum = 10000
while i <= lineCount:
    try:
        sumLines = sonarLines[i] + sonarLines[i+1] + sonarLines[i+2] # Sliding Window
        if sumLines > currentSum:
            task2Count = task2Count + 1
        currentSum = sumLines
    except IndexError:
        print(f"Total greater than previous window: {task2Count}")
    i += 1