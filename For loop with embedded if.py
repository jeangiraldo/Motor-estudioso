# -*- coding: utf-8 -*-

#For loop
devices=["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)

#For Loop with Embedded If
for item in devices:
    if "R" in item:
        print(item)

#For Loop to Create a New List
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
switches


