from sys import argv

inputfile = argv[1]

def parse_instruct(order):
    '''Turn an instruction into a step, prereq pair.'''
    line = order.split(" ")
    prereq, step = line[1], line[7]

    return step, prereq

def execute_instructions(instruct_list):
    '''Execute the instructions as specified for part 1'''
    done_steps = set()
    instruct_order = []
    num_steps = len(instruct_list.keys())
    while len(done_steps) < num_steps:
        candidates = []

        for key, value in instruct_list.items():
            if value.issubset(done_steps):
                candidates.append(key)

        candidates.sort()
        done_steps.add(candidates[0])
        instruct_order.append(candidates[0])
        del instruct_list[candidates[0]]

    return "".join(instruct_order)

instructions = {}

with open(inputfile) as file:
    for line in file:
        step, prereq = parse_instruct(line)

        if step in instructions.keys():
            instructions[step].add(prereq)
        else:
            instructions[step] = set(prereq)

        if prereq not in instructions.keys():
            instructions[prereq] = set()

print(execute_instructions(instructions))
