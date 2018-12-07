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

# Open the inputfile, and for each line, add it to the counter
with open(inputfile) as input:
    for freq in input:
        frequency = process_line(freq, frequency)

# Tell us the answer!
print(f"The final frequency is {frequency}!")
