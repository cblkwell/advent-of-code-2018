from sys import argv
import re

script, inputfile = argv

box_ids = []

# Create our array of box ids.
with open(inputfile) as f:
    for line in f:
        box_ids.append(line.strip())

found_boxes = False

while found_boxes == False:
    # Pop off the last box in the list, and make a list of characters.
    current_box = list(box_ids.pop())

    # For each character...
    for i in range(len(current_box)):

        # Create a copy of the list above.
        curr_search = current_box.copy()
     
        # Replace this character in the list with a period.
        curr_search[i] = '.'

        # Create a regex from the list we made above.
        search_str = re.compile(''.join(curr_search))

        # Now, for each other box remaining in the list...
        for box in box_ids:
            
            # Does the regex match the box id?
            if search_str.match(box):

                # If so, delete the period from the search list,
                # join the list into a string, and print success!
                # Then set found_boxes to True and leave the loop.
                del curr_search[i]
                common_char_str = ''.join(curr_search)
                print(f"The common string is {common_char_str}!")
                found_boxes = True
                break

        # Have we found the boxes yet? If so, get outta here!
        if found_boxes == True:
            break
            
