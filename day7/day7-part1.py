import os, sys

rules = {}

# construct rules
for line in open(os.path.join(sys.path[0], "input7.txt")):
    line = line.strip()[:-1] #cut the last dot
    parts = line.split("bags contain")
    keyBag = parts[0].strip()
    valueBags = parts[1].strip().split(",")
    valueBagDict = {}
    for valueBag in valueBags:
        valueBag = valueBag[:-4].strip() #cut the bags at the end
        valueBagParts = valueBag.split(" ")
        if valueBagParts[0] != "no":
            valueBagPartCount = int(valueBagParts[0])
            valueBagPartColor = valueBagParts[1] + " " + valueBagParts[2]
            valueBagDict[valueBagPartColor] = valueBagPartCount
    rules[keyBag] = valueBagDict


# process and find shiny gold bags holders
directShinyGoldHolders = []
for key in rules:
    if 'shiny gold' in rules[key].keys():
        directShinyGoldHolders.append(key)


shinyGoldHolders = directShinyGoldHolders
for holder in shinyGoldHolders:
    for key in rules:
        if holder in rules[key].keys():
            shinyGoldHolders.append(key)

uniqueShinyGoldHolders = []
for holder in shinyGoldHolders:
    if holder not in uniqueShinyGoldHolders:
        uniqueShinyGoldHolders.append(holder)

print(len(uniqueShinyGoldHolders))