import os, sys, copy

# build the program
theProgram = {}
lineNo = 0
for line in open(os.path.join(sys.path[0], "input8.txt")):
    parts = line.strip().split(" ")
    
    instruction = parts[0].strip()
    number = int(parts[1])

    theProgram[lineNo] = { "instruction": instruction, "number":number }
    lineNo +=1

def executeProgram(someProgram):
    # execute the program
    acc = 0
    nextLine = 0
    executedLines = []
    while nextLine not in executedLines:
        if nextLine >= len(someProgram):
            return {"acc":acc,"executedLines":executedLines, "cause":"normal"}
        executedLines.append(nextLine)
        if someProgram[nextLine]["instruction"] == "acc":
            acc += someProgram[nextLine]["number"]
            nextLine += 1
        elif someProgram[nextLine]["instruction"] == "nop":
            nextLine += 1
        elif someProgram[nextLine]["instruction"] == "jmp":
            nextLine += someProgram[nextLine]["number"]
            continue
    return {"acc":acc,"executedLines":executedLines, "cause":"loop"}

# change every jmp or nop to the other one by one and run again
for line in theProgram:
    modifiedProgram = copy.deepcopy(theProgram)
    if theProgram[line]["instruction"] == "jmp":
        modifiedProgram[line]["instruction"] = "nop"
    elif theProgram[line]["instruction"] == "nop":
        modifiedProgram[line]["instruction"] = "jmp"
    result = executeProgram(modifiedProgram)
    if result["cause"] == "normal":
        print(result["acc"])
        break
