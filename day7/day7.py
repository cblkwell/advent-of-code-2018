from sys import argv

inputfile = argv[1]

def parse_instruct(order):
    '''Turn an instruction into a step, prereq pair.'''
    line = order.split(" ")
    prereq, step = line[1], line[7]

    return step, prereq


def find_candidates(instructs, done_steps):
    '''Given a list of instructions and done steps, find candidates.'''
    candidates = []

    for key, value in instructs.items():
        if value.issubset(done_steps):
            candidates.append(key)
    
    candidates.sort() 

    return candidates

def simple_execution(instruct_list):
    '''Execute the instructions as specified for part 1'''
    done_steps = set()
    instruct_order = []
    num_steps = len(instruct_list.keys())

    while len(done_steps) < num_steps:
        candidates = find_candidates(instruct_list, done_steps)
        done_steps.add(candidates[0])
        instruct_order.append(candidates[0])
        del instruct_list[candidates[0]]

    return "".join(instruct_order)


def multi_worker(instruct_list, workers=2, skew=0)
    '''Execute the instructions as specified for part 2'''
    done_steps = set()
    num_steps = len(instruct_list.keys())
    time = 0
    work_queue = {}

    for worker in range(workers):
        work_queue[worker] = (None, 0)
    
    while len(done_steps) < num_steps:
        free_workers = []
        for worker in work_queue.keys():
            if work_queue[worker][0] != None and work_queue[worker][1] == time:
                done_steps.add(work_queue[worker][0])
                del instruct_list[work_queue[worker][0]]
                
            if work_queue[worker][1] <= time:
                free_workers.append(worker)

        if len(free_workers) = 0:
            time += 1
        else:
            candidates = find_candidates(instruct_list, done_steps)
        
            while len(candidates) > 0 and len(free_workers) > 0:
                job = candidates.pop(0)
                job_time = ord(job) - 64
                assignee = free_workers.pop()
                work_queue[assignee] = (job, job_time + skew + time)
        

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

print(simple_execution(instructions))
