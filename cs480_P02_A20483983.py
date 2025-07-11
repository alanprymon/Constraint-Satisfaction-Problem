import sys

def get_zones() -> list:
    file = open('zones.csv', 'rt')
    zones = file.read()
    file.close()
    zones = zones.split('\n')
    zones.pop()
    zones[0] = zones[0].split(',')
    zones[0].pop(0)
    zones[1] = zones[1].split(',')
    zones[1].pop(0)
    #print(zones)
    return zones

def get_parks() -> list:
    file = open('parks.csv', 'rt')
    parks = file.read()
    file.close()
    parks = parks.split('\n')
    parks.pop()
    parks[0] = parks[0].split(',')
    parks[0].pop(0)
    parks[1] = parks[1].split(',')
    parks[1].pop(0)
    #print(parks)
    return parks

def get_distances_matrix() -> (list, list):
    file = open('driving2.csv', 'rt')
    axis = file.readline().replace('\n', '').split(',')
    axis.pop(0)
    distances = []
    for x in file.readlines():
        line = x.replace('\n', '').split(',')
        line.pop(0)
        distances.append(line)
    # print(axis)
    # print(distances)
    return axis, distances

def get_distance(at: str, to: str, distances: (list,list)) -> int:
    axis = distances[0]
    distances = distances[1]
    for i in range(len(axis)):
        if axis[i] == at:
            at_index = i
        if axis[i] == to:
            to_index = i
    return int(distances[at_index][to_index])

def get_possible_next(at:str, zones: list, distances: (list, list)) -> list:
    for i in range(len(zones[0])):
        if at == zones[0][i]:
            at_zone = int(zones[1][i])
    possible = []
    for i in range(len(zones[1])):
        if at_zone + 1 == int(zones[1][i]):
            if get_distance(at, zones[0][i], distances) > -1:
                possible.append(zones[0][i])
    return possible

def is_final_zone(at: str, zones: list) -> bool:
    for i in range(len(zones[0])):
        if at == zones[0][i]:
            at_zone = int(zones[1][i])
    if at_zone == 12:
        return True
    else:
        return False

def get_num_parks(at: str, parks: list) -> int:
    for i in range(len(parks[0])):
        if at == parks[0][i]:
            return int(parks[1][i])
    print('ERROR: bad arguement: get_num_parks')
    exit(-1)

def backtracking_search(initial: str, min_parks: int, zones: list, parks: list, distance_matrix: (list, list)) -> list:
    return backtrack(initial, min_parks, 0, zones, parks, distance_matrix).split(',')

def backtrack(at: str, min_parks: int, current_parks: int, zones: list, parks: list, distance_matrix: (list, list)) -> str:
    if is_final_zone(at, zones) and min_parks <= current_parks + get_num_parks(at, parks):
        return at
    possible = get_possible_next(at, zones, distance_matrix) #gets a list of possibles next one instead of just one like in the psuedocode
    for value in possible: # get_possible_next is already in alphabetical order so no need to sort it
        # value is already consistent here
        result = backtrack(value, min_parks, current_parks + get_num_parks(at, parks), zones, parks, distance_matrix)
        if not result.isnumeric():
            return at + ',' + result
    return '0'


if __name__ == '__main__':
    if not len(sys.argv) == 3:#checking that the number of arguements is correct
        print('ERROR: Not enough or too many input arguments.')
        exit(-1)
    initial = sys.argv[1]
    if initial.isalpha():#checking that the first arguement is only letters
        initial = initial.upper()
    else:
        print('ERROR: bad initial argument.')
        exit(-1)
    num_of_parks = sys.argv[2]
    if not num_of_parks.isnumeric():#checking that the second arguemnt is only numbers
        print('ERROR: bad num_of_parks argument.')
        exit(-1)

    zones = get_zones()
    parks = get_parks()
    distance_matrix = get_distances_matrix()
    # print(str(get_distance('AZ', 'NV', distance_matrix)))
    # print(get_possible_next('AZ', zones, distance_matrix))
    # print(str(get_num_parks('CA', parks)))

    path = backtracking_search(initial, int(num_of_parks), zones, parks, distance_matrix)
    # print(path)
    if path[0].isalpha(): # not empty list aka path exists
        path_cost = 0
        for i in range(len(path) - 1):
            path_cost += get_distance(path[i], path[i + 1], distance_matrix)
        parks_visited = 0
        for x in path:
            parks_visited += get_num_parks(x, parks)
        print("Prymon, Alan, A20483983 solution:\nInitial state: " + initial + "\nMinimum number of parks: " + num_of_parks + '\nSolution path: ' + str(path) + '\nNumber of states on a path: ' + str(len(path)) + '\nPath cost: ' + str(path_cost) + '\nNumber of national parks visited: ' + str(parks_visited))
    else:
        print("Prymon, Alan, A20483983 solution:\nInitial state: " + initial + "\nMinimum number of parks: " + num_of_parks + '\nSolution path: FAILURE: NO PATH FOUND\nNumber of states on a path: 0\nPath cost: 0\nNumber of national parks visited: 0')