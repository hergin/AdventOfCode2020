import os, sys, math

def findRowNumber(encodedColumnRow):
    lower = 0
    upper = 127
    for c in encodedColumnRow[:-3]:
        if c == "F":
            upper = math.floor((lower + upper)/2)
        if c == "B":
            lower = math.ceil((lower + upper)/2)
    return lower

def findColumnNumber(encodedColumnRow):
    lower = 0
    upper = 7
    for c in encodedColumnRow[7:]:
        if c == "L":
            upper = math.floor((lower + upper)/2)
        if c == "R":
            lower = math.ceil((lower + upper)/2)
    return lower

def findSeatID(encodedColumnRow):
    return findRowNumber(encodedColumnRow)*8+findColumnNumber(encodedColumnRow)

highest = 0
for line in open(os.path.join(sys.path[0], "input5.txt")):
    seatID = findSeatID(line.strip())
    if seatID > highest:
        highest = seatID

print(highest)