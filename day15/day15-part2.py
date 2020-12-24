import os, sys

startingNumbers = list(map(int,open(os.path.join(sys.path[0], "input15.txt")).readline().strip().split(',')))

lastIndices = {}

index = 0
for number in startingNumbers:
    lastIndices[number] = {}
    lastIndices[number]["last"] = index
    lastIndices[number]["previous"] = -1
    index += 1

lastNumber = startingNumbers[-1]


def calculateNextNumber(i):
    global lastNumber
    if lastIndices[lastNumber]["previous"] == -1:
        # firstTime
        lastNumber = 0
    else:
        lastIndex = i-1
        indexOfLastNumberBeforeThat = lastIndices[lastNumber]["previous"]
        lastNumber = lastIndex - indexOfLastNumberBeforeThat

    if lastNumber in lastIndices:
        lastIndices[lastNumber]["previous"] = lastIndices[lastNumber]["last"]
    else:
        lastIndices[lastNumber] = {}
        lastIndices[lastNumber]["previous"] = -1
    lastIndices[lastNumber]["last"] = i
    return lastNumber

for i in range(len(startingNumbers),30000000):
    calculateNextNumber(i)

print(lastNumber)