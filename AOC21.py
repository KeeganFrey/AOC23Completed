import re

def printsmap(smap):
    vert = len(smap)
    hor = len(smap[0])
    for i in range(vert):
        tstr = ""
        for j in range (hor):
            tstr = tstr + smap[i][j]
        print(tstr)


def createNs(smap,x,y,w,h):
    if smap[y][x] == 'S':
        #u 2
        if not y <= 1 and (smap[y-1][x] != '#'):
            if smap[y-2][x] != 'S' and smap[y-2][x] != 'O' and smap[y-2][x] != 'N' and smap[y-2][x] != '#':
                smap[y-2][x] = 'N'
        #r 1 u 1
        if y != 0 and x+1 != w and (smap[y-1][x] != '#' or smap[y][x+1] != '#'):
            if smap[y-1][x+1] != 'S' and smap[y-1][x+1] != 'O' and smap[y-1][x+1] != 'N' and smap[y-1][x+1] != '#':
                smap[y-1][x+1] = 'N'
        #r 2
        if not x >= w-2 and (smap[y][x+1] != '#'):
            if smap[y][x+2] != 'S' and smap[y][x+2] != 'O' and smap[y][x+2] != 'N' and smap[y][x+2] != '#':
                smap[y][x+2] = 'N'
        #r 1 d 1
        if y+1 != h and x+1 != w and (smap[y+1][x] != '#' or smap[y][x+1] != '#'):
            if smap[y+1][x+1] != 'S' and smap[y+1][x+1] != 'O' and smap[y+1][x+1] != 'N' and smap[y+1][x+1] != '#':
                smap[y+1][x+1] = 'N'
        #d 2
        if not y >= h-2 and (smap[y+1][x] != '#'):
            if smap[y+2][x] != 'S' and smap[y+2][x] != 'O' and smap[y+2][x] != 'N' and smap[y+2][x] != '#':
                smap[y+2][x] = 'N'
        #l 1 d 1
        if y+1 != h and x != 0 and (smap[y+1][x] != '#' or smap[y][x-1] != '#'):
            if smap[y+1][x-1] != 'S' and smap[y+1][x-1] != 'O' and smap[y+1][x-1] != 'N' and smap[y+1][x-1] != '#':
                smap[y+1][x-1] = 'N'
        #l 2 
        if not x <= 1 and (smap[y][x-1] != '#'):
            if smap[y][x-2] != 'S' and smap[y][x-2] != 'O' and smap[y][x-2] != 'N' and smap[y][x-2] != '#':
                smap[y][x-2] = 'N'
        #l 1 u 1
        if y != 0 and x != 0 and (smap[y-1][x] != '#' or smap[y][x-1] != '#'):
            if smap[y-1][x-1] != 'S' and smap[y-1][x-1] != 'O' and smap[y-1][x-1] != 'N' and smap[y-1][x-1] != '#':
                smap[y-1][x-1] = 'N'


filepath = "input21.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

smap = []
for line in lines:
    seperated = re.split(r'\n',line)
    tli = []
    for ch in seperated[0]:
        tli.append(ch)
    smap.append(tli)

x = 0
y = 0
sx = 0
sy = 0
w = len(smap[0])
h = len(smap)
for lists in smap:
    x = 0
    for c in lists:
        if smap[y][x] == 'S':
            sx = x
            sy = y
        x+=1
    y+=1

createNs(smap,sx,sy,w,h)
i = 0
j = 0
while i < h:
    j=0
    while j < w:
        if smap[i][j] == 'S':
            smap[i][j]='O'
        elif smap[i][j] == 'N':
            smap[i][j]='S'
        j+=1
    i+=1
count = 31
while count > 0:
    x = 0
    y = 0
    for li in smap:
        x=0
        for c in li:
            if c == 'S':
                createNs(smap,x,y,w,h)
            x+=1
        y+=1
    i = 0
    j = 0
    while i < h:
        j=0
        while j < w:
            if smap[i][j] == 'S':
                smap[i][j]='O'
            elif smap[i][j] == 'N':
                smap[i][j]='S'
            j+=1
        i+=1
    count-=1
i = 0
j = 0
while i < h:
    j=0
    while j < w:
        if smap[i][j] == 'S':
            smap[i][j]='O'
        elif smap[i][j] == 'N':
            smap[i][j]='S'
        j+=1
    i+=1

i = 0
j = 0
count = 0
while i < h:
    j=0
    while j < w:
        if smap[i][j] == 'O':
            count+=1
        j+=1
    i+=1
printsmap(smap)
print(count)