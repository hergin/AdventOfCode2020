import os, sys, math

lines = open(os.path.join(sys.path[0], "input13.txt")).readlines()

buses = lines[1].strip().split(',')

indexAndBusId = {}

for i in range(len(buses)):
    if buses[i]!='x':
        indexAndBusId[i] = int(buses[i])

print(indexAndBusId)





# increase the numbers by MAX so that there will be less steps
maxValue = 0
maxIndex = -1
for index in indexAndBusId:
    if indexAndBusId[index] > maxValue:
        maxValue = indexAndBusId[index]
        maxIndex = index

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

del indexAndBusId[maxIndex]
step=2
#nextNumber = maxValue*2
nextNumber = 242975950306751
while True:
    broken = False

    for index in indexAndBusId:
        if (nextNumber+index-maxIndex) % indexAndBusId[index] != 0:
            broken = True
            break
    if not broken:
        print("found at",nextNumber-maxIndex,"with step:",step)
        break

    step+=1
    nextNumber+=maxValue 


'''
find a number that
    it is divisible by first item
    +1 of it is divisible by second item
    +2 of it is divisible by third item
    etc.

'''

'''
67,7,59,61 -> 754018     =   2 x 17 x 67 x 331

n   % 67 = 0        n   = 67a       a=11254
n+1 %  7 = 0        n+1 =  7b       b=107717
n+2 % 59 = 0        n+2 = 59c       c=12780
n+3 % 61 = 0        n+3 = 61d       d=12361

n^4 + .... = 67*7*59*61*abcd
           = 1687931 * abcd
'''

'''
67,7,x,59,61 -> 1261476        =   2^2 x 3^2 x 67 x 523

n   % 67 = 0
n+1 % 7  = 0
n+3 % 59 = 0
n+4 % 61 = 0
'''

'''
67,x,7,59,61 -> 779210         =   2 x 5 x 67 x 1163
'''

'''
17,x,13,19 -> 3417      =    3 x 17 x 67

{0: 17, 2: 13, 3: 19}

n   % 17 = 0           n = 17a          a=201     = 3 x 67
n+2 % 13 = 0           n = 13b-2        b=263     = 263
n+3 % 19 = 0           n = 19c-3        c=180     = 2^2 x 3^2 x 5
'''