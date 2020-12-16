import os, sys

directions = ['N','W','S','E']

eastPosition = 10
northPosition = 1
currentDirection = 'E'

shipEastPosition = 0
shipNorthPosition = 0

def turnRight(amount):
    global currentDirection
    global eastPosition
    global northPosition
    currentDirection = directions[directions.index(currentDirection)-int(amount/90)]
    counter = int(amount/90)
    while counter > 0:
        counter-=1
        if eastPosition >=0 and northPosition >=0:
            eastPosition = -eastPosition
        elif eastPosition >0 and northPosition <0:
            eastPosition = -eastPosition
        elif eastPosition <=0 and northPosition <=0:
            eastPosition = -eastPosition
        elif eastPosition <0 and northPosition >0:
            eastPosition = -eastPosition
        temp = eastPosition
        eastPosition = northPosition
        northPosition = temp

def turnLeft(amount):
    turnRight(360-amount)

def moveForward(amount):
    move(currentDirection,amount)

def moveBackward(amount):
    moveForward(-amount)

def moveShipForward(amount):
    global shipEastPosition
    global shipNorthPosition
    shipNorthPosition += amount*northPosition
    shipEastPosition += amount*eastPosition

def move(someDirection, amount):
    global eastPosition
    global northPosition
    if someDirection == 'E':
        eastPosition += amount
    elif someDirection == 'W':
        eastPosition -= amount
    elif someDirection == 'N':
        northPosition += amount
    elif someDirection == 'S':
        northPosition -= amount

for line in open(os.path.join(sys.path[0], "input12.txt")):
    
    command = line.strip()[0]
    amount = int(line.strip()[1:])
    if command == 'N' or command == 'S' or command == 'W' or command == 'E':
        move(command,amount)
    elif command == 'F':
        moveShipForward(amount)
    elif command == 'B':
        moveBackward(amount)
    elif command == 'L':
        turnLeft(amount)
    elif command == 'R':
        turnRight(amount)
    

print(currentDirection," -> East ",eastPosition,", North ",northPosition)
print("Ship -> East ",shipEastPosition,", North ",shipNorthPosition)
print("manhattan: ",str(abs(shipEastPosition)+abs(shipNorthPosition)))
print("manhattan: ",str(abs(eastPosition)+abs(northPosition)))