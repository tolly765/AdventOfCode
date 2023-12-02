import re

def re_words_to_num(line):
    conditions = {"one": "o1e", "two": "t2o", "three": "th3ee", "four": "fo4r", "five": "fi5e", "six": "s6x", "seven": "se7en", "eight": "ei8ht", "nine": "n9ne"}
    conditions = dict((re.escape(k), v) for k, v in conditions.items()) # Apply any regex escapes to the dict above
    pattern = re.compile("|".join(conditions.keys())) # Compile dict above into python regex
    line = pattern.sub(lambda m: conditions[re.escape(m.group(0))], line) # Search for the keys above in the dict and replace with the appropriate value
    return line

def part1(input_text):
    print("Running Part 1")
    # Code goes here
    values = []
    for line in input_text:
        charlist = []
        for char in line:
            if char.isdigit():
                charlist.append(char)
        values.append(int(charlist[0] + charlist[-1]))
    return ("Part 1: " + str(sum(values)))
    

def part2(input_text):
    print("Running Part 2")
    # Code goes here
    values = []
    for line in input_text:
        # Run twice to pick up on neighbouring values (e.g. oneight -> o1eight -> o1ei8ht)
        # Quirk with using re to replace values at once
        proc_line = re_words_to_num(line)
        proc_line = re_words_to_num(proc_line)
        
        charlist = []
        for char in proc_line:
            if char.isdigit():
                charlist.append(char)
        values.append(int(charlist[0] + charlist[-1]))
    return ("Part 2: " + str(sum(values)))


# TODO Make this cleaner, it makes me sad :(
with open("../input/Day1.txt", "r") as input:
    print(part1(input))

with open("../input/Day1.txt", "r") as input:
    print(part2(input))

