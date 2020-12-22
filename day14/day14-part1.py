import os, sys, math

def applyMask(value,mask):
    maskedValue = 0
    tempValue = value

    for i in range(0,len(mask)):
        maskedValue *= 2
        twoPowerI = 2**(35-i)
        if mask[i] == '1':
            maskedValue += 1
        elif mask[i] == 'X':
            if tempValue >= twoPowerI:
                maskedValue += 1
        if tempValue >= twoPowerI:
                tempValue -= twoPowerI
                
    return maskedValue

currentMask = ""
memory = {}

for line in open(os.path.join(sys.path[0], "input14.txt")):
    values = line.strip().split(' ')

    if values[0] == "mask":
        currentMask = values[2]
    else:
        memoryIndex = int(values[0][4:][:-1])
        value = int(values[2])
        valueAfterMask = applyMask(value, currentMask)
        memory[memoryIndex] = valueAfterMask
        print("mask:",currentMask,"memoryIndex:",memoryIndex,"value:",value,"maskedValue:",valueAfterMask)

#print(memory)
print("Result",sum(memory.values()))