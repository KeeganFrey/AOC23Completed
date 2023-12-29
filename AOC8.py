import re

filepath = "input8.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

instructions = ""
nodes = []
for line in lines:
    seperated = re.split(r'[ \n=(),]', line)
    seperated = [item for item in seperated if item != ""]
    l = len(seperated)
    if l==1:
        instructions = instructions+seperated[0]
    elif l!=0:
        nodes.append(seperated)

nnl = 0
for arr in nodes:
        if arr[0] == "AAA":
            break
        nnl+=1
count = 0
strtofind ="AAA"
leninstr = len(instructions) 
while strtofind!="ZZZ":
    l = instructions[count % leninstr]
    strtofind = ""
    if l =='L':
        strtofind = nodes[nnl][1]
    else:
        strtofind = nodes[nnl][2]
    nnl = 0
    for arr in nodes:
        if arr[0] == strtofind:
            break
        nnl+=1
    count+=1

print(count)
