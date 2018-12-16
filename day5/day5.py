from sys import argv
import re

inputfile = argv[1]

with open(inputfile) as file:
    polymer = list(file.read().rstrip())
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

print(f"The reacted polymer is {''.join(reacted_polymer)}")
print(f"The length of the reacted polymer is {len(reacted_polymer)}.")
