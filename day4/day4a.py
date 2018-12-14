from sys import argv
from operator import itemgetter
import re

script, inputfile = argv

# We're probably going to want some function to parse the events in
# the logfile.
def parse_event(event):
    # The event can be parsed with our friend the regex, and can be
    # one of three types: guard on duty, guard asleep, guard up.
    # First, get the time elements and payload.
    ts_parser = re.compile(r'^\[(.*)\s(.*)\]\s(.*)\n')
    date, time, payload = ts_parser.match(event).groups()

    # For the date, we can just get rid of the punctuation, we just
    # need it as a uid, basically.
    date = date.replace('-','')

    # For the time, we want the hour and minute separately.
    hour, minute = time.split(":")
    
    timestamp = (int(date), int(hour), int(minute))

    # For the payload, if it starts with "Guard", we know it's a
    # shift change.
    shift_parser = re.compile(r'Guard (.*) begins shift')
    if shift_parser.match(payload):
        event_type = shift_parser.match(payload).group(1)
    # The other two cases are a little easier:
    elif payload == 'falls asleep':
        event_type = 'sleep'
    elif payload == 'wakes up':
        event_type = 'wake'

    return [timestamp, event_type]

# Now we need a function to process all those events.
def process_log(event_log):
    guard = re.compile(r'^#.*')
    processed_log = {}
    # The main loop here will take us through the events one by one.
    index = 0
    while index < len(event_log):
        # We're looking for a guard first. We also know the first
        # item in any log will be a guard, so we can leave on_duty
        # empty initially.
        if guard.match(event_log[index][1]):
            on_duty = event_log[index][1]
            print(f"Guard {on_duty} is now on duty!")
            # Is the guard in our processed log yet? If not, add
            # them.
            if on_duty not in processed_log:
                processed_log[on_duty] = []
                # Fill it with zeros for the minutes!
                for i in range(60):
                    processed_log[on_duty].append(0)
            # If we found a guard, increment the index by one so we
            # look at the next line.
            index += 1
        elif event_log[index][1] == 'sleep':
            # If the guard fell asleep, set the start time for his
            # sleep.
            sleep_time = event_log[index][0][2]
            print(f"{on_duty} fell asleep at {sleep_time}!")
            # Increment the counter.
            index += 1
        elif event_log[index][1] == 'wake':
            # The guard woke up! We can fill things in now:
            wake_time = event_log[index][0][2]
            print(f"{on_duty} woke up at {wake_time}!")
            # For every minute between falling asleep and waking up,
            # increment the minute counter by 1.
            for i in range(sleep_time, wake_time):
                processed_log[on_duty][i] += 1
            # Increment the counter.
            index += 1

    # Now we have processed log! Return it:
    return processed_log

def sleepiest_guard(guard_log):
    sleepiest = [ "", 0 ]
    # For each guard in our log...
    for guard in guard_log:
        # If this guard has slept longer than the current winner...
        if sum(guard_log[guard]) > sleepiest[1]:
            # Then they're the sleepiest!
            sleepiest = [ guard, sum(guard_log[guard]) ]
    
    return sleepiest
        

guard_log = []
    
with open(inputfile) as f:
    for line in f:
        guard_log.append(parse_event(line))

guard_record = process_log(sorted(guard_log))

sleeper = sleepiest_guard(guard_record)[0]

print(f"The sleepiest guard is {sleeper}!")
print(f"Their sleepiest minute was {guard_record[sleeper].index(max(guard_record[sleeper]))}.")
