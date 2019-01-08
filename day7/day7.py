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
        if value.issubset(done_steps) and key not in done_steps:
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

class Elf:
    def __init__(self):
        self.job = None
        self.finish_time = 0
        self.busy = False

    def assign_job(self, job, finish_time):
        global current_time
        self.job = job
        self.finish_time = finish_time
        self.busy = True

    def finish_job(self):
        self.job = None
        self.finish_time = 0
        self.busy = False

def full_process(instruct_list, workers, skew):
    '''A unified process for working through a list of instructions.'''
    num_steps = len(instruct_list.keys())
    current_time = 0
    done_steps = set()
    
    # Build a list of workers
    elves = [Elf()] * workers   

    while len(done_steps) < num_steps:
        free_workers = []
        for elf in elves:
            if elf.finish_time == current_time and elf.job != None:
                print(f"{current_time}: An elf finished job {elf.job}")
                print(f"{current_time}: Adding {elf.job} to done_steps")
                done_steps.add(elf.job)
                print(f"{current_time}: done_steps is {done_steps}")
                elf.finish_job()
                free_workers.append(elf)
            elif elf.busy == False:
                free_workers.append(elf)

        if len(free_workers) == 0:
            print(f"{current_time}: All workers busy")
            current_time += 1
        else:
            candidates = find_candidates(instruct_list, done_steps)
    
            while len(free_workers) > 0 and len(candidates) > 0:
                print(f"{current_time}: There's {len(free_workers)} free workers")
                worker_elf = free_workers.pop()
                new_job = candidates.pop(0)
                job_done = ord(new_job) - 64 + skew + current_time
                worker_elf.assign_job(new_job, job_done)
                print(f"{current_time}: Assigned elf {worker_elf} job {new_job} to finish at {job_done}")

            current_time += 1
    
    step_order = "".join(done_steps)
    return step_order, current_time
    
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

with open(inputfile) as file:
    for line in file:
        step, prereq = parse_instruct(line)
print(instructions)
print(full_process(instructions, 2, 0))
