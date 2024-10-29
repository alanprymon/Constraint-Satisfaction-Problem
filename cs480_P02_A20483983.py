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

def get_distances() -> (list, list):
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
    axis, distances = get_distances()

    

    print("Prymon, Alan, A20483983 solution:\nInitial state: " + initial + "\nMinimum number of parks: " + num_of_parks)