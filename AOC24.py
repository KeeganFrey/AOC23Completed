import re

def tosystemofeqs(row):
    xyc = []
    xyc.append((-1)*row[4])
    xyc.append(row[3])
    xyc.append(row[3]*row[1]-row[4]*row[0])
    return xyc

def cramersrule(eq1,eq2):
    x = eq1[2]*eq2[1]-eq2[2]*eq1[1]
    y = eq1[0]*eq2[2]-eq2[0]*eq1[2]
    s = complex(x,y)
    return s

def futurecolisioninrange(hails, eqa, eqb, min, max):
    seqa = tosystemofeqs(hails[eqa])
    seqb = tosystemofeqs(hails[eqb])
    rval = 0 
    d = seqa[0]*seqb[1]-seqa[1]*seqb[0]
    if d != 0:
        ns = cramersrule(seqa,seqb)
        xpos = ns.real/d
        ypos = ns.imag/d
        tvxa = (xpos-hails[eqa][0])/hails[eqa][3]
        tvxb = (xpos-hails[eqb][0])/hails[eqb][3]
        tvya = (ypos-hails[eqa][1])/hails[eqa][4]
        tvyb = (ypos-hails[eqb][1])/hails[eqb][4]
        if tvxa>0 and tvxb>0 and tvya>0 and tvyb>0:
            if xpos>=min and xpos<=max and ypos>=min and ypos <=max:
                rval+=1
    return rval

filepath = "input24.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

hails = []
for line in lines:
    seperated = re.split(r'[ \n@,]', line)
    seperated = [item for item in seperated if item != ""]
    li = []
    for ch in seperated:
        li.append(int(ch))
    print(li)
    hails.append(li)

min = 200000000000000
max = 400000000000000
i = 0
j = 0
count = 0
l = len(hails)
total = 0
while i < l:
    j = i
    while j < l:
        if i!=j:
            count += futurecolisioninrange(hails,i,j,min, max)
            total+=1
        j+=1
    i+=1

print(count)
