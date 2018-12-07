from sys import argv
# Counter will create a dictionary that pairs characters with counts --
# perfect for what we need!
from collections import Counter

script, inputfile = argv

def process_line(line, threes, twos):
    # Use counter to get us a dict of the letter frequencies.
    counts = Counter(line)
    add_three = False
    add_two = False

    # For each element of the dict...
    for i in counts:
        # Are there three in the same line?  If so, increment that counter.
        if counts[i] == 3:
            add_three = True
        # Are there two in the same line? If so, increment that counter.
        elif counts[i] == 2:
            add_two = True
    
    if add_three == True:
        threes += 1
   
    if add_two == True:
        twos += 1
    return threes, twos

# Zero out our counts
three_count = 0
two_count = 0

# Open the file and read through it, processing each line.
with open(inputfile) as f:
    for line in f:
        three_count, two_count = process_line(line, three_count, two_count)

checksum = three_count * two_count

print(f"The checksum is {checksum}!")
