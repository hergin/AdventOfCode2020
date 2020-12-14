import os, sys

sum = 0
onegroup = ""
firstSet = False
for line in open(os.path.join(sys.path[0], "input6.txt")):
    if line.strip() != "" and not firstSet:
        onegroup = line.strip()
        firstSet = True
    elif line.strip() != "" and firstSet:
        newonegroup = ""
        for char in onegroup:
            if char in line.strip():
                newonegroup += char
        onegroup = newonegroup
    else:
        uniqueQs = {}
        for char in onegroup:
            uniqueQs[char] = 0
        sum += len(uniqueQs)
        onegroup = ""
        firstSet = False

if onegroup.strip() != "":
    uniqueQs = {}
    for char in onegroup:
        uniqueQs[char] = 0
    sum += len(uniqueQs)

print(sum)