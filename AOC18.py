import re

def fillnexttodr(pmap,vert,hor, ctr):
    count = 0
    i = 1
    j = 1
    while i<vert-1:
        while j<hor-1:
            if pmap[i][j] =='.':
                if pmap[i+1][j] ==ctr or pmap[i-1][j] ==ctr or pmap[i][j+1] ==ctr or pmap[i][j-1] ==ctr:
                    pmap[i][j] = ctr
                    count +=1
            j+=1
        i+=1
        j=1
    i = 1
    j = 1
    while j<hor-1:
        while i<vert-1:
            if pmap[i][j] =='.':
                if pmap[i+1][j] ==ctr or pmap[i-1][j] ==ctr or pmap[i][j+1] ==ctr or pmap[i][j-1] ==ctr:
                    pmap[i][j] = ctr
                    count +=1
            i+=1
        j+=1
        i=1
    return count

def fillnexttoul(pmap,vert,hor,ctr):
    count = 0
    i = vert-2
    j = hor-2
    while i>0:
        while j>0:
            if pmap[i][j] =='.':
                if pmap[i+1][j] ==ctr or pmap[i-1][j] ==ctr or pmap[i][j+1] ==ctr or pmap[i][j-1] ==ctr:
                    pmap[i][j] = ctr
                    count +=1
            j-=1
        i-=1
        j = hor-2
    i = vert-1
    j = hor-1
    while j>0:
        while i>0:
            if pmap[i][j] == '.':
                if pmap[i+1][j] ==ctr or pmap[i-1][j] ==ctr or pmap[i][j+1] ==ctr or pmap[i][j-1] ==ctr:
                    pmap[i][j] = ctr
                    count +=1
            i -= 1
        j -=1
        i = vert-2
    return count

#Not implemented correctly, a bug exists when defining the undecided edges, but it works well enough for the problem
def uedge(pmap,vert,hor):
    for i in range(vert):
        for j in range (hor):
            if pmap[i][j] == '#':
                if (pmap[i+1][j] == '.' and pmap[i-1][j] == '.')or(pmap[i][j+1] == '.' and pmap[i][j-1] == '.'):
                    pmap[i][j] = 'U'
                elif ((pmap[i+1][j] == '#'or pmap[i+1][j] == 'U') and pmap[i-1][j] == '.')or(pmap[i+1][j] == '.' and (pmap[i-1][j] == '#'or pmap[i-1][j] == 'U'))or((pmap[i][j+1] == '#' or pmap[i][j+1] == 'U')and pmap[i][j-1] == '.')or (pmap[i][j+1] == '.' and (pmap[i][j-1] == '#' or pmap[i][j-1] == 'U')):
                    pmap[i][j] = 'U'
                
def ucorner(pmap,vert,hor):
    for i in range(vert-2):
        for j in range (hor-2):
            if pmap[i][j] == '#':
                if pmap[i+1][j] =='U' or pmap[i-1][j] =='U' or pmap[i][j+1] =='U' or pmap[i][j-1] =='U':
                    pmap[i][j] = 'U'

def finishfill(pmap,vert,hor):
    for i in range(vert):
        for j in range (hor):
            if pmap[i][j] == '.':
                pmap[i][j] = '█'

filepath = "input18.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

maxd = 0
maxu = 0
maxl = 0
maxr = 0
v = 1
h = 1
for item in lines:
    seperated = re.split(r'[ \n]',item)
    seperated = [item for item in seperated if item != ""]
    if seperated[0] == 'U':
        v -= int(seperated[1])
        if v<maxu:
            maxu = v
    elif seperated[0] == 'D':
        v += int(seperated[1])
        if v>maxd:
            maxd = v
    elif seperated[0] == 'R':
        h += int(seperated[1])
        if h>maxr:
            maxr = h
    elif seperated[0] == 'L':
        h -= int(seperated[1])
        if h<maxl:
            maxl = h

vert = (-1)*maxu + maxd+6
hor = maxr + (-1)*maxl +6
pmap = [['.' for _ in range(hor)] for _ in range(vert)]
a = (-1)*maxu+3
b = (-1)*maxl+3
na = a
nb = b

for item in lines:
    seperated = re.split(r'[ \n]',item)
    seperated = [item for item in seperated if item != ""]
    if seperated[0] == 'U':
        na = a - int(seperated[1])
        while a>na:
            pmap[a][b] = '#'
            a-=1
    elif seperated[0] == 'D':
        na = a + int(seperated[1])
        while a<na:
            pmap[a][b] = '#'
            a+=1
    elif seperated[0] == 'R':
        nb = b + int(seperated[1])
        while b<nb:
            pmap[a][b] = '#'
            b+=1
    elif seperated[0] == 'L':
        nb = b - int(seperated[1])
        while b>nb:
            pmap[a][b] = '#'
            b-=1

for i in range(hor):
    pmap[0][i] = '█'
    pmap[vert-1][i] = '█'

for i in range(vert):
    pmap[i][0] = '█'
    pmap[i][hor-1] = '█'

fills = 1
while(fills != 0):
    fills = fillnexttodr(pmap,vert, hor,'█')
    fills += fillnexttoul(pmap,vert, hor,'█')

uedge(pmap,vert,hor)
ucorner(pmap,vert,hor)

fills = 1
while(fills != 0):
    fills = fillnexttodr(pmap,vert, hor,'#')
    fills += fillnexttoul(pmap,vert, hor,'#')

finishfill(pmap,vert,hor)
sum = 0
for i in range(vert):
    for j in range (hor):
        if pmap[i][j] == '#':
            sum+=1
        elif pmap[i][j] == 'U':
            pmap[i][j] = '#'
            sum+=1
print(sum)
