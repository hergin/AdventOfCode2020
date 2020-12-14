
import os, sys
for l1 in open(os.path.join(sys.path[0], "input1.txt")):
    for l2 in open(os.path.join(sys.path[0], "input1.txt")):
        if int(l1.strip())+int(l2.strip()) == 2020:
            print(int(l1.strip())*int(l2.strip()))