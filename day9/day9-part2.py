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

        pos = 0
        for num1 in numbers:
            remainingOfTheList = numbers[pos:]
            pos+=1
            sum =0
            newList = []
            for remaining in remainingOfTheList:
                sum += remaining
                newList.append(remaining)
                if sum == number and len(newList)!=1:
                    print(max(newList)+min(newList))
                    pass
                elif sum > number:
                    break
        break