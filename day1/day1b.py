from sys import argv

# Get the inputfile from the command line
script, inputfile = argv

# We want to define a function to process these lines; add the int of
# the line to the sum.
def process_line(line, sum):
    sum += int(line)
    return sum

# Zero out the counter
frequency = 0
freqval = {0}
done = False

# While done is False, keep looping through the file until you get a
# second frequency value.
while done == False: 
    # Open the inputfile, and for each line, add it to the counter
    with open(inputfile) as input:
        for freq in input:
            frequency = process_line(freq, frequency)
            # If the frequency is not in the set of frequency values
            if frequency not in freqval:
                # ...then add it to the set
                freqval.add(frequency)
            # Otherwise, set done to True and break the loop.
            else:
                done = True
                break

# Tell us the answer!
print(f"The duplicate frequency is {frequency}!")
