import re

filepath = "input4.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

msum = 0
nextten = [1,1,1,1,1,1,1,1,1,1]
for item in lines:
    seperated = re.split(r'[ ]',item)
    seperated = [item for item in seperated if item != ""]
    spl = 0
    ln = []
    for word in seperated:
        if word == '|':
            break
        if word.isdigit():
            ln.append(int(word))
        spl +=1
    seplen = len(seperated)
    i = spl+1
    points = 0
    while i<seplen:
        for num in ln:
            if num == int(seperated[i]):
                points +=1
        i+=1
    multiplier = nextten[0] 
    nextten[0] = nextten[1]
    nextten[1] = nextten[2]
    nextten[2] = nextten[3]
    nextten[3] = nextten[4]
    nextten[4] = nextten[5]
    nextten[5] = nextten[6]
    nextten[6] = nextten[7]
    nextten[7] = nextten[8]
    nextten[8] = nextten[9]
    nextten[9] = 1
    for i in range(points):
        nextten[i] += multiplier
    msum+=multiplier

print(msum)
    