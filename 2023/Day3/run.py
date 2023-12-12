import re

def bothparts(input_text):
    # Code goes here
    sanitised_input = []
    #! Deviating from template as it is easier to reuse the structure of part 1 for part 2
    # Sanitise input and convert to list
    for dirty_line in input:
        sanitised_line = dirty_line.strip()
        sanitised_input.append(sanitised_line)
    # Create sets to store found symbols and symbol locations
    symbols = set()
    symbol_locations = set()
    gear_locations = set()

    # Discovering symbols and their X/Y coordinates and saving them
    for y, line in enumerate(sanitised_input):
        for x, char in enumerate(line):
            if char != "." and not (char.isnumeric()):
                symbols.add(char)
                symbol_locations.add((x,y))
                # For Part 2 - find gears and save their X/Y coords
                if char == "*":
                    gear_locations.add((x,y))
    

    number_list = [] # Storing list of found numbers, their X/Y coords and their 
    active_number = False # Bool to check if a number is present
    width = len(sanitised_input[0]) # Get width of lines in the schematic

    for y, l in enumerate(sanitised_input):
        for x, c in enumerate(l):
            if not(active_number) and (c == "." or c in symbols):
                continue
            elif not(active_number) and c.isnumeric():
                current_number = c
                active_number = True
                NewX1 = x
            elif active_number and (c == "." or c in symbols):
                NewNum = int(current_number)
                NewX2 = x-1
                number_list.append((NewNum, NewX1, NewX2, y))
                active_number = False
                current_number = ""
            elif active_number and c.isnumeric():
                current_number += c
                if x == width - 1:
                    NewNum = int(current_number)
                    NewX2 = x
                    number_list.append((NewNum, NewX1, NewX2, y))
                    active_number = False
                    current_number = ""

    # Iterate through the number list, find all of the symbols 
    answer1 = 0
    for number, X1, X2, Y in number_list:
        bordering_points = set()
        for y in range(Y-1,Y+2):
            for x in range(X1-1,X2+2):
                bordering_points.add((x, y))
        intersecting_points = symbol_locations & bordering_points
        if len(intersecting_points) > 0:
            answer1 += number
    
    answer2 = 0
    for GX, GY in gear_locations:
        gear_borders = set()
        gear_neighbours = []
        for x in range(GX-1,GX+2):
            for y in range(GY-1,GY+2):
                gear_borders.add((x,y))
        for Number, X1, X2, Y in number_list:
            if (X1, Y) in gear_borders or (X2, Y) in gear_borders:
                gear_neighbours.append(Number)
        if len(gear_neighbours) == 2:
            N1, N2 = gear_neighbours
            answer2 += N1*N2
    
    return (f"Part 1: {answer1} \nPart 2: {answer2}")
    

with open("../input/Day3.txt", "r") as input:
    print(bothparts(input))

