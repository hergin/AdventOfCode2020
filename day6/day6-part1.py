import os, sys

sum = 0
onegroup = ""
for line in open(os.path.join(sys.path[0], "input6.txt")):
    if line.strip() != "":
        onegroup += line.strip()
    else:
        uniqueQs = {}
        for char in onegroup:
            uniqueQs[char] = 0
        print(uniqueQs)
        sum += len(uniqueQs)
        onegroup = ""

if onegroup.strip() != "":
    uniqueQs = {}
    for char in onegroup:
        uniqueQs[char] = 0
    sum += len(uniqueQs)

print(sum)