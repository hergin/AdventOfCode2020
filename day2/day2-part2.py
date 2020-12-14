import os, sys

valid=0
for line in open(os.path.join(sys.path[0], "input2.txt")):
    parts = line.strip().split(":")
    firstparts = parts[0].split("-")
    lowerlimit = int(firstparts[0])
    secondparts = firstparts[1].split(" ")
    upperlimit = int(secondparts[0])
    letter = secondparts[1]
    password = parts[1].strip()

    if password[lowerlimit-1]==letter and password[upperlimit-1]!=letter:
        print(line.strip())
        valid+=1
    if password[lowerlimit-1]!=letter and password[upperlimit-1]==letter:
        print(line.strip())
        valid+=1
print(valid)