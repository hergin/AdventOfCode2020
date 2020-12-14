import os, sys

count=0
x=0
for line in open(os.path.join(sys.path[0], "input3.txt")):
    extendedline = line.strip()
    while x >= len(extendedline):
        extendedline += line.strip()
    if extendedline[x] == "#":
        count+=1
    x+=3

print(count)