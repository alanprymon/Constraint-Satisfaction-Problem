import sys

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

    

    print("Prymon, Alan, A20483983 solution:\nInitial state: " + initial + "\nMinimum number of parks: " + num_of_parks)