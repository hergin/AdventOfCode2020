import os, sys

mult = 1
for i in [1,3,5,7]:
    x=0
    count=0
    for line in open(os.path.join(sys.path[0], "input3.txt")):
        extendedline = line.strip()
        while x >= len(extendedline):
            extendedline += line.strip()
        if extendedline[x] == "#":
            count+=1
        x+=i

    mult *= count

    if i==1:
        mult *= count * 0.5

print(mult)