from sys import argv

inputfile = argv[1]

def define_grid(coord_list):
    x_coords = set()
    y_coords = set()
    for coord in coord_list:
        x_coords.add(coord[0])
        y_coords.add(coord[1])
    
    left_bound = min(x_coords)
    right_bound = max(x_coords)
    bottom_bound = min(y_coords)
    top_bound = max(y_coords)

    return left_bound, right_bound, bottom_bound, top_bound

def man_dist(coord1, coord2):
    dist = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    return dist

def find_closest(coords, point):
    distances = {}
 
    for coord in coords:
#        print(f"Finding distance between {point} and {coord}")
        dist = man_dist(coord, point)
        distances[coord] = dist

    min_dist = None
    closest_pt = None
    for point, distance in distances.items():
        if min_dist == None or distance < min_dist:
            min_dist = distance
            closest_pt = point
#            print(f"min_dist is now {min_dist} for coord {closest_pt}") 
    
    # Now we need to make sure there's not multiple coords at
    # the min distance.
    count = 0
    for dist in distances.values():
        if dist == min_dist:
            count += 1

    # If there is, nothing is the closest point.
    if count > 1:
        closest_pt = None

    return closest_pt


def find_largest(coord_list, grid):
    grid_descript = {}
    left_bound, right_bound, bottom_bound, top_bound = grid

    possible_winners = coord_list.copy()
    print("Looking for largest in this coord list:")
    print(coord_list)
    print("The possible winners list is:")
    print(possible_winners)

    # First, patrol the border; any point which is closest to a
    # border *can't* be a winner.
    for x in range(left_bound, right_bound + 1):
        for y in (bottom_bound, top_bound):
            closest_pt = find_closest(coord_list, (x,y))
            if closest_pt != None and closest_pt in possible_winners:
                print(f"{closest_pt} is along the side at {(x,y)}")
                possible_winners.remove(closest_pt)

    for y in range(bottom_bound, top_bound + 1):
        for x in (left_bound, right_bound):
            closest_pt = find_closest(coord_list, (x,y))
            if closest_pt != None and closest_pt in possible_winners:
                print(f"{closest_pt} is along the side at {(x,y)}")
                possible_winners.remove(closest_pt)

    # Build a dict to keep track of closest points.
    tally = {}
    for candidate in possible_winners:
        tally[candidate] = []    

    for y in range(bottom_bound + 1, top_bound):
        for x in range(left_bound + 1, right_bound):
            closest_pt = find_closest(coord_list, (x,y))
            if closest_pt != None and closest_pt in possible_winners:
                tally[closest_pt].append((x,y))

    max_area = 0
    largest_pt = None
    for key in tally:
        if len(tally[key]) > max_area:
            largest_pt = key
            max_area = len(tally[key])

    return largest_pt, max_area

def find_region(coord_list, grid):
    left_bound, right_bound, bottom_bound, top_bound = grid
    region_size = 0

    for y in range(bottom_bound, top_bound + 1):
        for x in range(left_bound, right_bound + 1):
            total_dist = 0
            point = (x,y)
            for coord in coord_list:
                total_dist = total_dist + man_dist(coord, point) 
            
            if total_dist < 10000:
                region_size += 1

    return region_size
    
            
coords = []

with open(inputfile) as file:
    for line in file:
        x, y = line.rstrip().split(", ")
        x, y = int(x), int(y)
        coords.append((x,y))

grid = define_grid(coords)
print(find_largest(coords, grid))
print(find_region(coords, grid))
