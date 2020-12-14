import os, sys

def check(password):
    fields = onepassport.split(" ")
    idArray = {}
    for field in fields:
        if field.strip()!="":
            idArray[field.strip().split(":")[0]] = field.strip().split(":")[1]
    print(idArray,end='\n')
    if "byr" in idArray and len(idArray["byr"]) == 4 and int(idArray["byr"]) >= 1920 and int(idArray["byr"]) <= 2002 and \
        "iyr" in idArray and len(idArray["iyr"]) == 4 and int(idArray["iyr"]) >= 2010 and int(idArray["iyr"]) <= 2020 and \
            "eyr" in idArray and len(idArray["eyr"]) == 4 and int(idArray["eyr"]) >= 2020 and int(idArray["eyr"]) <= 2030 and \
                "hgt" in idArray and (("cm" in idArray["hgt"] and int(idArray["hgt"][:-2])>=150 and int(idArray["hgt"][:-2])<=193) or ("in" in idArray["hgt"] and int(idArray["hgt"][:-2])>=59 and int(idArray["hgt"][:-2])<=76)) and \
                    "hcl" in idArray and idArray["hcl"][0] == "#" and len(idArray["hcl"])==7 and any(c.isnumeric() or c in ['a','b','c','d','e','f'] for c in idArray["hcl"][1:]) and \
                        "ecl" in idArray and idArray["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"] and \
                            "pid" in idArray and len(idArray["pid"])==9 and any(c.isnumeric() for c in idArray["pid"]):
        return True
    return False

valid=0
onepassport = ""
for line in open(os.path.join(sys.path[0], "input4.txt")):
    if line.strip() != "":
        onepassport += " " + line.strip()
    else:
        if check(onepassport):
            valid+=1
        onepassport=""

if onepassport.strip() != "" and check(onepassport):
    valid+=1

print(valid)