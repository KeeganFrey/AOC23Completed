import re

def nextlayer(valarr,firstval,arrout):
        length = len(valarr)
        i = 0
        while i<length-1:
            arrout.append(int(valarr[i+1])-int(valarr[i]))
            if i == 0:
                firstval.append(int(valarr[i+1])-int(valarr[i]))
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
    firstval = [int(seperated[0])]
    nextlayer(seperated,firstval,newvals)
    while not allzeros(newvals):
        temparr = []
        nextlayer(newvals,firstval,temparr)
        newvals = temparr
    l = len(firstval)
    subtractor = 0
    for i in range(l):
        subtractor=firstval[l-i-1]-subtractor
    sum+=subtractor
     
     
print(sum)