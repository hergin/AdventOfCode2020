import os, sys

# build the program
theProgram = {}
lineNo = 0
for line in open(os.path.join(sys.path[0], "input8.txt")):
    parts = line.strip().split(" ")
    
    instruction = parts[0].strip()
    number = int(parts[1])

    theProgram[lineNo] = { "instruction": instruction, "number":number }
    lineNo +=1

# execute the program
nextLine = 0
executedLines = []
acc = 0
while nextLine not in executedLines:
    executedLines.append(nextLine)
    if theProgram[nextLine]["instruction"] == "acc":
        acc += theProgram[nextLine]["number"]
        nextLine += 1
    elif theProgram[nextLine]["instruction"] == "nop":
        nextLine += 1
    elif theProgram[nextLine]["instruction"] == "jmp":
        nextLine += theProgram[nextLine]["number"]

print(acc)