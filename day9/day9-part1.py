import os, sys

numbers = []
for line in open(os.path.join(sys.path[0], "input9.txt")):
    numbers.append(int(line.strip()))


numberPosition = 0
for number in numbers:
    tempNumberList = numbers[max(numberPosition,25)-25:max(numberPosition,0)]
    numberPosition+=1

    found = False
    for tempNumber in tempNumberList:
        for nextTemp in tempNumberList:
            if tempNumber != nextTemp and tempNumber + nextTemp == number:
                #print(number," = ",tempNumber," + ",nextTemp)
                found = True

    if numberPosition>25 and not found:
        print(number)
        break