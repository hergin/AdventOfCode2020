import os, sys

directions = ['N','W','S','E']

eastPosition = 0
northPosition = 0
currentDirection = 'E'

def turnRight(amount):
    global currentDirection
    currentDirection = directions[directions.index(currentDirection)-int(amount/90)]

def turnLeft(amount):
    global currentDirection
    currentDirection = directions[(directions.index(currentDirection)+int(amount/90))%4]

def moveForward(amount):
    move(currentDirection,amount)

def moveBackward(amount):
    moveForward(-amount)

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
        moveForward(amount)
    elif command == 'B':
        moveBackward(amount)
    elif command == 'L':
        turnLeft(amount)
    elif command == 'R':
        turnRight(amount)
    

print(currentDirection," -> East ",eastPosition,", North ",northPosition)
print("manhattan: ",str(abs(eastPosition)+abs(northPosition)))