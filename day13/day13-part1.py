import os, sys

lines = open(os.path.join(sys.path[0], "input13.txt")).readlines()

mytimestamp = int(lines[0].strip())

buses = lines[1].strip().split(',')


def findFirstHigherMultiplicant(baseNumber,ID):
    result = 0
    while result < baseNumber:
        result += ID
    return result

nextBusIDs = []
nextBusTimes = []
for bus in buses:
    if bus != "x":
        firstHigher = findFirstHigherMultiplicant(mytimestamp,int(bus))
        nextBusTimes.append(firstHigher)
        nextBusIDs.append(bus)

time = min(nextBusTimes)
busID = nextBusIDs[nextBusTimes.index(time)]
print("Bus ID:",busID,"at time",time)
print("Result: ",int(busID)*(time-mytimestamp))