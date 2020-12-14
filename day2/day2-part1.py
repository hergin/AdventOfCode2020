import os, sys

valid=0
for line in open(os.path.join(sys.path[0], "input2.txt")):
    parts = line.split(":")
    firstparts = parts[0].split("-")
    lowerlimit = int(firstparts[0])
    secondparts = firstparts[1].split(" ")
    upperlimit = int(secondparts[0])
    letter = secondparts[1]
    password = parts[1].strip()
    count=0
    for i in range(len(password)):
        if password[i]==letter:
            count+=1
    if count >= lowerlimit and count <= upperlimit:
        print(line)
        valid+=1
print(valid)