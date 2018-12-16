from sys import argv
import re
import string

inputfile = argv[1]

def react_polymer(input_poly):
    polymer = list(input_poly)
    index = 0
    reacted_polymer = []
    same_unit = re.compile(r'(\w)\1', re.IGNORECASE)
    while index < len(polymer):
        if len(reacted_polymer) < 1:
            reacted_polymer.append(polymer[index])
            index += 1
        else:
            chain_end = [reacted_polymer[-1], polymer[index]]
            chain_joined = "".join(chain_end)
            if same_unit.match(chain_joined) and reacted_polymer[-1] != polymer[index]:
                del reacted_polymer[-1]
                index += 1
            else:
                reacted_polymer.append(polymer[index])
                index += 1
    
    return reacted_polymer


with open(inputfile) as file:
    polymer = file.read().rstrip()
    reacted_polymer = react_polymer(polymer)
    shortest_polymer = tuple()
    for element in string.ascii_lowercase:
        cap_element = element.capitalize()
        new_polymer = polymer.replace(element, "").replace(cap_element, "")
        print(new_polymer)
        new_polymer = react_polymer(new_polymer)
        if len(shortest_polymer) == 0:
            shortest_polymer = (new_polymer, len(new_polymer))
        else:
            if len(new_polymer) < shortest_polymer[1]:
                shortest_polymer = (new_polymer, len(new_polymer)) 
      
        

print(f"The reacted polymer is {''.join(reacted_polymer)}")
print(f"The length of the reacted polymer is {len(reacted_polymer)}.")
print(f"But the shortest improved polymer is {''.join(shortest_polymer[0])}")
print(f"It is {shortest_polymer[1]} long.")
