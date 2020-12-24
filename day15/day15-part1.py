import os, sys

startingNumbers = list(map(int,open(os.path.join(sys.path[0], "input15.txt")).readline().strip().split(',')))

turn = startingNumbers.copy()

def findNextNumber(i):
    lastNumber = turn[-1]
    indexOfTheLastNumberInTurn = turn.index(lastNumber)
    if indexOfTheLastNumberInTurn == i-1:
        # firstTime
        return 0
    else:
        lastIndex = i-1
        dummyTurn = turn[:-1]
        dummyTurn.reverse()
        indexOfLastNumberBeforeThat = dummyTurn.index(lastNumber)
        return lastIndex - (len(dummyTurn) - 1 - indexOfLastNumberBeforeThat)


for i in range(len(startingNumbers), 2020):
    turn.append(findNextNumber(i))

print(turn[-1])