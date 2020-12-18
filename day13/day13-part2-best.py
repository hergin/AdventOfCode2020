# check day13-helper.xlsx and day13-solution-approach.gif to understand

import os, sys, math

lines = open(os.path.join(sys.path[0], "input13.txt")).readlines()

buses = lines[1].strip().split(',')

indexAndBusId = {}

for i in range(len(buses)):
    if buses[i]!='x':
        indexAndBusId[i] = int(buses[i])


maxNumber = max(indexAndBusId.values())

sequenceList = range(0,maxNumber)

numbersAndMods = {}

for key in indexAndBusId:
    currentNumber = indexAndBusId[key]
    currentNumberPortionOfFirstNumberList = sequenceList[:currentNumber]

    modsList = []
    for number in currentNumberPortionOfFirstNumberList:
        modsList.append((number+key)%currentNumber)

    numbersAndMods[currentNumber] = modsList

minMods = numbersAndMods[min(numbersAndMods.keys())]


start = 0
step = 1
maxNumber = max(numbersAndMods.keys())
maxMod = numbersAndMods[maxNumber]
del numbersAndMods[maxNumber]

while len(numbersAndMods.keys()) > 0:
    nextMax = max(numbersAndMods.keys())
    nextMaxKey = -1
    for key in indexAndBusId:
        if indexAndBusId[key]==nextMax:
            nextMaxKey = key
            break
    del numbersAndMods[nextMax]

    sequenceNumbersWhereMaxMod0 = []
    for i in range(maxNumber*nextMax):
        if maxMod[i%maxNumber] == 0:
            sequenceNumbersWhereMaxMod0.append((i*step+start))
    
    nextMaxModList = []
    for i in sequenceNumbersWhereMaxMod0:
        nextMaxModList.append((i+nextMaxKey)%nextMax)
    
    step = sequenceNumbersWhereMaxMod0[1]-sequenceNumbersWhereMaxMod0[0]
    start = sequenceNumbersWhereMaxMod0[0]
    maxNumber = nextMax
    maxMod = nextMaxModList

finalValue = start

for mod in maxMod:
    if mod == 0:
        break
    finalValue += step

print("found at",finalValue)