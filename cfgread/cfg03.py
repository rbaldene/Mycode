#!/usr/bin/env python3
## create file object in "r"ead mode
line_count=0
for line in configlist:
    if line !="\n":
        line_count +=1

with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(line_count)
