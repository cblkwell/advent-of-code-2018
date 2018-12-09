from sys import argv

script, inputfile = argv

# Process the line to determine the swatch overlap.
def process_input(line, taken_set, duped_set, counter):

    # This is a lot of hoop jumping to get rid of the things from
    # the line we don't need and get just the location and size of
    # the swatch in two separate arrays.
    cleandata = line.strip().split(' @ ')[1].split(': ')
    corner = cleandata[0].split(',')
    swatch_area = cleandata[1].split('x')

    # Now we figure out what coordinates are in the swatch and
    # and compare them to the set of coordinates already allocated.
    # I suspect there's a better way to do this with some sort of
    # python math function.
    for width in range(int(corner[0]) + 1, int(corner[0]) + int(swatch_area[0]) + 1):
        for length in range(int(corner[1]) + 1, int(corner[1]) + int(swatch_area[1]) + 1):
            # If the coordinate is in the set, increment the counter.
            if (width,length) in taken_set:
                # If it hasn't already been counted, count it and add
                # it to the duped set.
                if (width, length) not in duped_set:
                    duped_set.add((width,length))
                    counter += 1
            # Otherwise, add the new coordinate to the set.
            else:
                taken_set.add((width,length))
    
    return taken_set, duped_set, counter

allocated_swatches = set()
duplicate_swatches = set()
dupes = 0

# Process the file line by line.
with open(inputfile) as f:
    for line in f:    
        allocated_swatches, duplicate_swatches, dupes = process_input(line, allocated_swatches, duplicate_swatches, dupes)

print(f"There are {dupes} duplicate reservations.")
