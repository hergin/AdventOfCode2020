import os, sys

valid=0
onepassport = ""
for line in open(os.path.join(sys.path[0], "input4.txt")):
    if line.strip() != "":
        onepassport += " " + line.strip()
    else:
        fields = onepassport.split(" ")
        idArray = []
        for field in fields:
            idArray.append(field.strip().split(":")[0])
        if "byr" in idArray and "iyr" in idArray and "eyr" in idArray and "hgt" in idArray and "hcl" in idArray and "ecl" in idArray and "pid" in idArray:
            valid+=1
        onepassport=""

if onepassport.strip() != "":
    fields = onepassport.split(" ")
    idArray = []
    for field in fields:
        idArray.append(field.strip().split(":")[0])
    if "byr" in idArray and "iyr" in idArray and "eyr" in idArray and "hgt" in idArray and "hcl" in idArray and "ecl" in idArray and "pid" in idArray:
        valid+=1

print(valid)