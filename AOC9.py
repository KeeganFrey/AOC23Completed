import re

def nextlayer(valarr,lastval,arrout):
        length = len(valarr)
        i = 0
        while i<length-1:
            arrout.append(int(valarr[i+1])-int(valarr[i]))
            if i == length-2:
                lastval.append(int(valarr[i+1])-int(valarr[i]))
            i+=1

def allzeros(arrin):
    for nums in arrin:
        if nums!= 0:
            return False
    return True

filepath = "input9.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    seperated = re.split(r'[ \n=(),]', line)
    seperated = [item for item in seperated if item != ""]
    newvals = []
    lastval = [int(seperated[len(seperated)-1])]
    nextlayer(seperated,lastval,newvals)
    while not allzeros(newvals):
        temparr = []
        nextlayer(newvals,lastval,temparr)
        newvals = temparr
    tempnum = 0
    for num in lastval:
        tempnum+=num
    sum+=tempnum
     
     
print(sum)