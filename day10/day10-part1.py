import os, sys

voltages = []
for line in open(os.path.join(sys.path[0], "input10.txt")):
    voltages.append(int(line.strip()))

voltages.sort()

voltages.append(max(voltages)+3) #largest

print(voltages)

current = 0
counts = {1:0,2:0,3:0}

while len(voltages) > 0:
    popped = voltages.pop(0)
    if popped-current < 4:
        counts[popped-current]+=1
        current = popped
    else:
        print("BROKEN")
        break

print(current)
print(counts)
print(counts[1]*counts[3])