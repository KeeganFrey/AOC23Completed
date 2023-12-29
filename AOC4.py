import re

filepath = "input4.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

pointsum = 0
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
                if points != 0:
                    points*=2
                else:
                    points = 1
        i+=1
    pointsum+=points

print(pointsum)
    