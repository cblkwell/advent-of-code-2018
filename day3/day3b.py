from sys import argv
import re

script, inputfile = argv

# Process the line.
def process_input(line, contenders, taken_swatches):

    # First, we need parse the swatch into a pair of lists that will
    # hold the location and area, so that we can compute the coords
    # covered by the new swatch.
    parser = re.compile(r'(?P<uid>#[0-9]*)\s@\s'
        r'(?P<corner>[0-9]*,[0-9]*): '
        r'(?P<swatch_area>[0-9]*x[0-9]*)')
    uid, unclean_corner, unclean_area = parser.match(line).groups()
    
    corner = unclean_corner.split(',')
    swatch_area = unclean_area.split('x')
    new_contender = True

    # Now we have what we need. We'll need to iterate over the
    # coords in the swatch like before. The way we were doing it
    # before won't work, so this time we'll do something a little
    # different.
    for width in range(int(corner[0]) + 1, int(corner[0]) + int(swatch_area[0]) + 1):
        for length in range(int(corner[1]) + 1, int(corner[1]) + int(swatch_area[1]) + 1):
            coord = (width, length)
            # We have to use .get here because otherwise we get a
            # KeyError if it doesn't exist.
            if taken_swatches.get(coord, False):
                # We know this swatch is not a new candidate.
                new_contender = False
                # We also know that if there's only one element
                # in the set of swatches that uses that coordinate,
                # there's a chance it was a candidate; make sure we
                # take it out.
                if len(taken_swatches[coord]) == 1:
                    # There's no good way to get the only element
                    # of a set, it seems.
                    (loser,) = taken_swatches[coord]
                    if loser in contenders:
                        contenders.remove(loser)
                # We should also make sure we add this swatch to the
                # list of swatches on that coord.
                taken_swatches[coord].add(uid)
            # If the coordinate is not in the dict, then we add the
            # coordinate and the uid as its value in a set.
            else:
                taken_swatches[coord] = {uid}
    
    # Okay! We've gone through that whole list. If we're still a new
    # candidate, add it to the set!
    if new_contender == True:
        contenders.add(uid)

    return contenders, taken_swatches
    
candidates = set()
allocated_swatches = {}

# Process the file line by line.
with open(inputfile) as f:
    for line in f:    
        candidates, allocated_swatches = process_input(line, candidates, allocated_swatches)
        
print(f"The winning swatch is: {candidates}")
