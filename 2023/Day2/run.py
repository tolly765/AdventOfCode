import os
import re
# Only 12 red, 13 green and 14 blue

def part1(input_text):
    # Code goes here
    successful_games = []
    id = 1 #? Game ID counting. Yes, I know this is a programming sin but the IDs start at 1 :(
    for line in input_text:
        round = line.strip().split(": ") # Split the lines and remove the Game ID as we're counting internally
        pulls = re.split("; |, ", round[1]) # Split each game into individual pulls
        # Probably a much nicer way of doing this, but this works
        red_yes = True
        blue_yes = True
        green_yes = True
        # Iterative loop to check each split 
        for pull in pulls: # Iterate through each individual pull from the bag
            if "red" in pull:
                entries = pull.split(" ") # Split each pull to check the value 
                if int(entries[0]) > 12: #! Red requires 12 cubes or less
                    red_yes = False
            elif "green" in pull:
                entries = pull.split(" ") # Split each pull to check the value 
                if int(entries[0]) > 13: #! Green requires 13 cubes or less
                    blue_yes = False
            elif "blue" in pull:
                entries = pull.split(" ") # Split each pull to check the value 
                if int(entries[0]) > 14: #! Blue requires 14 cubes or less
                    green_yes = False
            else:
                print("Broken...")
        # If none of the conditions for the cubes are broken, add the game ID to a list
        if red_yes and green_yes and blue_yes: 
            successful_games.append(id)
        id = id + 1 # Iterate counter
    # Print the sum of all the IDs
    return (f"Part 1: {sum(successful_games)}")

def part2(input_text):
    # Code goes here
    power_sets = []
    id = 1 #? Game ID counting. Yes, I know this is a programming sin but the IDs start at 1 :(
    for line in input_text:
        round = line.strip().split(": ") # Split the lines and remove the Game ID as we're counting internally
        pulls = re.split("; |, ", round[1]) # Split each game into individual pulls
        #* Set up lists for each game
        red_count = []
        green_count = []
        blue_count = []
        # Iterative loop to check each split 
        for pull in pulls: # Iterate through each individual pull from the bag
            if "red" in pull:
                entries = pull.split(" ")
                red_count.append(int(entries[0])) # Add all of the red values to a list
            elif "green" in pull:
                entries = pull.split(" ")
                green_count.append(int(entries[0])) # Add all of the green values to a list
            elif "blue" in pull:
                entries = pull.split(" ")
                blue_count.append(int(entries[0])) # Add all of the blue values to a list
            else: 
                print("Broken again...")
        # Find the largest number of cubes present in each counter, multiply them together and append to a new list
        power_sets.append((max(red_count) * max(green_count) * max(blue_count))) 
    # Add all of the multiplied values together and return result
    return (f"Part 2: {sum(power_sets)}") 

# TODO Make this cleaner, it makes me sad :(
with open("../input/Day2.txt", "r") as input:
    print(part1(input))

with open("../input/Day2.txt", "r") as input:
    print(part2(input))

