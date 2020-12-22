import os, sys, math

def applyMask(value,mask):
    addresses = [0]
    tempValue = value

    for i in range(0,len(mask)):
        for j in range(len(addresses)):
            addresses[j] *= 2
        twoPowerI = 2**(35-i)
        if mask[i] == '1':
            for j in range(len(addresses)):
                addresses[j] += 1
        elif mask[i] == '0':
            if tempValue >= twoPowerI:
                for j in range(len(addresses)):
                    addresses[j] += 1
        elif mask[i] == 'X':
            newAddresses = []
            for address in addresses:
                newAddresses.append(address+1)
            addresses += newAddresses
        if tempValue >= twoPowerI:
                tempValue -= twoPowerI
                
    return addresses

currentMask = ""
memory = {}

for line in open(os.path.join(sys.path[0], "input14.txt")):
    values = line.strip().split(' ')

    if values[0] == "mask":
        currentMask = values[2]
    else:
        memoryIndex = int(values[0][4:][:-1])
        value = int(values[2])
        memoryIndexesAfterMask = applyMask(memoryIndex, currentMask)
        for index in memoryIndexesAfterMask:
            memory[index] = value
        print("mask:",currentMask,"memoryIndex:",memoryIndex,"value:",value,"adresses:",memoryIndexesAfterMask)

#print(memory)
print("Result",sum(memory.values()))