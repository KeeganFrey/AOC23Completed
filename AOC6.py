import re
import math 

filepath = "input6.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

timedist = []
for line in lines:
    seperated = re.split(r'[ \n]', line)
    seperated = [item for item in seperated if item != ""]
    timedist.append(seperated)

i=1
sumli = []
while i<len(timedist[0]):
    t = int(timedist[0][i])
    d = int(timedist[1][i])
    sumli.append(int(t/2+math.sqrt((t**2)/4-d))-int(t/2-math.sqrt((t**2)/4-d)))
    i+=1

product = 1
for num in sumli:
    product*=num

print(product)
