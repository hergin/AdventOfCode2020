import os, sys, math

lines = open(os.path.join(sys.path[0], "input13.txt")).readlines()

buses = lines[1].strip().split(',')

indexAndBusId = {}

for i in range(len(buses)):
    if buses[i]!='x':
        indexAndBusId[i] = int(buses[i])


firstNumber = indexAndBusId[0]
del indexAndBusId[0]


maxNumber = max(indexAndBusId.values())


firstNumberList = []

for i in range(0,maxNumber):
    firstNumberList.append(i*firstNumber)

numbersAndMods = {}

for key in indexAndBusId:
    currentNumber = indexAndBusId[key]
    currentNumberPortionOfFirstNumberList = firstNumberList[:currentNumber]

    modsList = []
    for number in currentNumberPortionOfFirstNumberList:
        modsList.append((number+key)%currentNumber)

    numbersAndMods[currentNumber] = modsList

step = 0

while True:
    broken = False
    for key in numbersAndMods:
        if numbersAndMods[key][step%key] != 0:
            broken = True
            break

    if not broken:
        print("Found at step",step,"and number is",(step*firstNumber))
        break

    step+=1