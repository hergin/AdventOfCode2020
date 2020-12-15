import os, sys, copy

def createGrid():
    grid = []
    for line in open(os.path.join(sys.path[0], "input11.txt")):
        grid.append(list(line.strip()))
    return grid

def printGrid(aGrid):
    for i in range(0,len(aGrid)):
        for j in range(0,len(aGrid[i])):
            print(aGrid[i][j],end='')
        print()
    
def findAdjacents(i,j,theGrid):
    adjacents = []
    if i>0 and j>0 and i<len(theGrid)-1 and j<len(theGrid[0])-1:
        # normal case
        adjacents = [[i-1,j-1],[i,j-1],[i+1,j-1],[i-1,j],[i+1,j],[i-1,j+1],[i,j+1],[i+1,j+1]]
    if i==0 and j>0 and i<len(theGrid)-1 and j<len(theGrid[0])-1:
        adjacents = [[i,j-1],[i+1,j-1],[i+1,j],[i,j+1],[i+1,j+1]]
    if i>0 and j==0 and i<len(theGrid)-1 and j<len(theGrid[0])-1:
        adjacents = [[i-1,j],[i+1,j],[i-1,j+1],[i,j+1],[i+1,j+1]]
    if i>0 and j>0 and i==len(theGrid)-1 and j<len(theGrid[0])-1:
        adjacents = [[i-1,j-1],[i,j-1],[i-1,j],[i-1,j+1],[i,j+1]]
    if i>0 and j>0 and i<len(theGrid)-1 and j==len(theGrid[0])-1:
        adjacents = [[i-1,j-1],[i,j-1],[i+1,j-1],[i-1,j],[i+1,j]]
    if i==0 and j==0 and i<len(theGrid)-1 and j<len(theGrid[0])-1:
        adjacents = [[i+1,j],[i,j+1],[i+1,j+1]]
    if i>0 and j>0 and i==len(theGrid)-1 and j==len(theGrid[0])-1:
        adjacents = [[i-1,j-1],[i,j-1],[i-1,j]]
    return adjacents

def empty_If_Occupied_And_4_orMore_Adjacent_Occupied(i,j,actualGrid,unchangedGrid):
    if unchangedGrid[i][j] == '#':
        adjacents = findAdjacents(i,j,actualGrid)
        count = 0
        for adjacent in adjacents:
            if unchangedGrid[adjacent[0]][adjacent[1]] == '#':
                count+=1
        if count>=4:
            actualGrid[i][j] = 'L'
            return True
    return False

def occupy_If_Empty_And_NoOccupied_Adjacent(i,j,actualGrid,unchangedGrid):
    if unchangedGrid[i][j] == 'L':
        adjacents = findAdjacents(i,j,actualGrid)
        for adjacent in adjacents:
            if unchangedGrid[adjacent[0]][adjacent[1]] == '#':
                return False
        actualGrid[i][j] = '#'
        return True
    return False

def checkOccupyAll(actualGrid):
    someChangeHappened = False
    unchangedGrid = copy.deepcopy(actualGrid)
    for i in range(0,len(actualGrid)):
        for j in range(0,len(actualGrid[i])):
            changed = occupy_If_Empty_And_NoOccupied_Adjacent(i,j,actualGrid,unchangedGrid)
            if changed:
                someChangeHappened = True
            
    unchangedGrid = copy.deepcopy(actualGrid)
    for i in range(0,len(actualGrid)):
        for j in range(0,len(actualGrid[i])):
            changed = empty_If_Occupied_And_4_orMore_Adjacent_Occupied(i,j,actualGrid,unchangedGrid)
            if changed:
                someChangeHappened = True

    return someChangeHappened

def loopOccupy(actualGrid):
    while checkOccupyAll(actualGrid):
        #printGrid(grid)
        #print()
        pass

def countOccupied(aGrid):
    sum = 0
    for i in range(0,len(aGrid)):
        for j in range(0,len(aGrid[i])):
            if aGrid[i][j] == '#':
                sum+=1
    return sum

grid = createGrid()
printGrid(grid)
print()
loopOccupy(grid)
printGrid(grid)

print(countOccupied(grid))