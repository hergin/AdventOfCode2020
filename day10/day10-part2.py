import os, sys, math

voltages = []
for line in open(os.path.join(sys.path[0], "input10.txt")):
    voltages.append(int(line.strip()))

voltages.append(0)
voltages.append(max(voltages)+3) #largest

voltages.sort()

print(voltages)

def findCombinations(series):
    totalNum = series[-1]-series[0]-1
    if totalNum == 1:
        return 2
    return int(math.factorial(totalNum)/(math.factorial(1)*math.factorial(totalNum-1)) \
        + math.factorial(totalNum)/(math.factorial(2)*math.factorial(totalNum-2)) \
            + 1)

print(findCombinations([4,5,6,7]))

position = 0
aOneChain = {"list":[],"startsWith2":False,"endWith2":False}
oneChainList = []
for i in range(position,len(voltages)-1):
    if voltages[position+1] - voltages[position] == 1:
        if position-1 >0 and voltages[position] - voltages[position-1] == 2:
            aOneChain["startsWith2"] = True
        aOneChain["list"].append(voltages[position])
    if voltages[position+1] - voltages[position] > 1:
        if position-1 >= 0 and voltages[position] - voltages[position-1] == 1:
            if position+1 < len(voltages)  and voltages[position+1] - voltages[position] == 2:
                aOneChain["endWith2"] = True
            aOneChain["list"].append(voltages[position])
        oneChainList.append(aOneChain)
        aOneChain =  {"list":[],"startsWith2":False,"endWith2":False}
    position+=1

print(oneChainList)

mult = 1
for oneChain in oneChainList:
    if len(oneChain["list"]) > 2:
        combinations = findCombinations(oneChain["list"])
        if oneChain["startsWith2"]:
            combinations += combinations/2
        if oneChain["endWith2"]:
            combinations += combinations/2
        if oneChain["startsWith2"] and oneChain["endWith2"]:
            combinations -= 1
        mult *= int(combinations)


print(mult)

# I left my notes under below just for reminder to myself how I did work on it :) They may not mean anything to you.

'''
algorithm
1lik gruplara ayir.
boyu 2 olanlari yoket.

her 1lik grup icin, findCombinations = X
Eger baslangicinda 2lik bir sayi daha ekliyse + X/2
Eger sonunda 2lik sayi ekliyse + X/2 - 1



'''

'''
count=0
position = 1
for i in range(position,len(voltages)-1):
    if voltages[position+1] - voltages[position] == 1 and voltages[position] - voltages[position-1] == 1:
        count+=1
    if voltages[position+1] - voltages[position] == 2 and voltages[position] - voltages[position-1] == 1:
        count+=1
    if voltages[position+1] - voltages[position] == 1 and voltages[position] - voltages[position-1] == 2:
        count+=1
    position+=1

print(int(math.pow(2,count)))
'''
'''
0       1       4       5       6       7       10      11      12      15      16      19      22
*--(1)--*--(3)--*--(1)--*--(1)--*--(1)--*--(3)--*--(1)--*--(1)--*--(3)--*--(1)--*--(3)--*--(3)--*

3 luk listelere ayir
0 1           4 5 6 7       10 11 12       15 16       19       22

1 ve 2 elemanlilari yok et
4 5 6 7       10 11 12

Geri kalanlar kendi icinde ne kadar degisik dizilebilir bul ve carp.
  2^2    *    2^1


0       2       4       5       6       7       10      11      12      15      16      19      22

0 2 4 5 6 7       10 11 12     15 16     19     22
0 2   5 6 7
0 2 4   6 7
0 2 4 5   7
0 2   5   7
0 2 4     7

0 2 4 5 6 7 9 12 13 14 17 18 21 24
1lik seri gruplarina ayir
4 5 6 7      12 13 14      17 18
2likleri sil.
4 5 6 7      12 13 14


4 5 6 7 9
4   6 7 9
4 5   7 9
4     7 9
4 5 6   9
4   6   9
  5 6 7 9
  5   7 9
  5 6   9


2 4 5 6   9
2   5 6 7 9
2   5   7 9
2   5 6   9
2 4   6   9



2 4 5 6 7 8 10
2 4   6 7 8 10
2 4 5   7 8 10
2 4 5 6   8 10
2 4     7 8 10
2 4   6   8 10
2 4 5     8 10

3un 1li combination + 3un 2li combination
3!/(1!*(3-1)!)     
3 + 3 + 1


for numbers from N to M
totalNums = M-N-1
return 


0       2       4       5       6       7
*--(2)--*--(2)--*--(1)--*--(1)--*--(1)--*

(ilk ve son haric)
Incoming and outgoing toplami 3 olan sayilar:  4
   "           "      toplami 2 olan sayilar:  5  and  6 



0 2 4 5 6 7 9 10 11
0 2   5 6 7 9 10 11  // 1 value can go
0 2 4   6 7 9 10 11
0 2 4 5   7 9 10 11
0 2 4 5 6   9 10 11
0 2 4 5 6 7   10 11
0 2 4 5 6 7 9    11
0 2   5   7 9 10 11  // 2 values can go
0 2   5 6   9 10 11
0 2   5 6 7   10 11
0 2   5 6 7 9    11
0 2 4   6 7 9 10 11
0 2 4     7 9 10 11
0 2 4   6   9 10 11
0 2 4   6 7   10 11
0 2 4   6 7 9    11
0 2 4 5     9 10 11
0 2 4 5   7   10 11
0 2 4 5   7 9    11
0 2 4 5 6   9    11
0 2   5   7   10 11 // 3 values can go
0 2   5   7 9    11
0 2 4     7   10 11
0 2 4     7 9    11
'''