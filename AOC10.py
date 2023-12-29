import re

def ltoblock(pmap,x,y):
    if pmap[y][x]== 'F':
        pmap[y][x] = '╔'
    elif pmap[y][x]== '7':
        pmap[y][x] = '╗'
    elif pmap[y][x] == '|':
        pmap[y][x] = '║'
    elif pmap[y][x]== 'J':
        pmap[y][x] = '╝'
    elif pmap[y][x]== 'L':
        pmap[y][x] = '╚'
    elif pmap[y][x] == '-':
        pmap[y][x] = '═'

def progress(pmap,x,y):
    width = len(pmap[0])
    height = len(pmap)
    if y+1 != height and pmap[y+1][x]== 'L' and (pmap[y][x]=='║' or pmap[y][x]=='╔' or pmap[y][x]=='╗'):
        y+=1 
    elif y+1 != height and pmap[y+1][x]== 'J' and (pmap[y][x]=='║' or pmap[y][x]=='╔' or pmap[y][x]=='╗'):
        y+=1
    elif y+1 != height and pmap[y+1][x] == '|' and (pmap[y][x]=='║' or pmap[y][x]=='╔' or pmap[y][x]=='╗'):
        y+=1
    elif y != 0 and pmap[y-1][x]== 'F' and (pmap[y][x]=='║' or pmap[y][x]=='╚' or pmap[y][x]=='╝'):
        y-=1
    elif y != 0 and pmap[y-1][x]== '7' and (pmap[y][x]=='║' or pmap[y][x]=='╚' or pmap[y][x]=='╝'):
        y-=1
    elif y != 0 and pmap[y-1][x] == '|' and (pmap[y][x]=='║' or pmap[y][x]=='╚' or pmap[y][x]=='╝'):
        y-=1
    elif x != 0 and pmap[y][x-1]== 'F' and (pmap[y][x]=='═' or pmap[y][x]=='╗' or pmap[y][x]=='╝'):
        x-=1
    elif x != 0 and pmap[y][x-1]== 'L' and (pmap[y][x]=='═' or pmap[y][x]=='╗' or pmap[y][x]=='╝'):
        x-=1
    elif x != 0 and pmap[y][x-1] == '-' and (pmap[y][x]=='═' or pmap[y][x]=='╗' or pmap[y][x]=='╝'):
        x-=1
    elif x+1 != width and pmap[y][x+1]== 'J' and (pmap[y][x]=='═' or pmap[y][x]=='╔' or pmap[y][x]=='╚'):
        x+=1
    elif x+1 != width and pmap[y][x+1]== '7' and (pmap[y][x]=='═' or pmap[y][x]=='╔' or pmap[y][x]=='╚'):
        x+=1
    elif x+1 != width and pmap[y][x+1] == '-' and (pmap[y][x]=='═' or pmap[y][x]=='╔' or pmap[y][x]=='╚'):
        x+=1
    ltoblock(pmap,x,y)
    return complex(x,y)

def testend(pmap,r1x,r2x,r1y,r2y):
    rval = False
    diffx = abs(r1x-r2x)
    diffy = abs(r1y-r2y)
    diff = diffx+diffy
    if diff>1:
        return rval
    if diffx == 1:
        if r1x-1==r2x and (pmap[r1y][r2x] == '╚' or pmap[r1y][r2x] == '╔' or pmap[r1y][r2x] == '═'):
            rval = True
        elif r1x+1==r2x and (pmap[r1y][r2x] == '╝' or pmap[r1y][r2x] == '╗' or pmap[r1y][r2x] == '═'):
            rval = True
        if r1y-1==r2y and (pmap[r2y][r1x] == '╝' or pmap[r2y][r1x] == '╚' or pmap[r2y][r1x] == '║'):
            rval = True
        elif r1y+1==r2y and (pmap[r2y][r1x] == '╔' or pmap[r2y][r1x] == '╗' or pmap[r2y][r1x] == '║'):
            rval = True
    else:
        return rval
    return rval

filepath = "input10.txt"
with open(filepath,'r') as file:
    lines = file.readlines()

instructions = ""
nodes = []
x = 0
y = 0
sx = 0
sy = 0
pmap = []
for line in lines:
    seperated = re.split(r'\n', line)
    seperated = [item for item in seperated if item != ""]
    x=0
    tmpli = []
    for chara in seperated[0]:
        tmpli.append(chara)
        if chara == 'S':
            sx=x
            sy=y
        x+=1
    y+=1
    pmap.append(tmpli)

r1y=sy
r1x=sx
r1count = 0
if pmap[sy-1][sx]== 'F':
    r1y-=1
    pmap[r1y][r1x] = '╔'
elif pmap[sy-1][sx]== '7':
    r1y-=1
    pmap[r1y][r1x] = '╗'
elif pmap[sy-1][sx] == '|':
    r1y-=1
    pmap[r1y][r1x] = '║'
elif pmap[sy+1][sx]== 'J':
    r1y+=1
    pmap[r1y][r1x] = '╝'
elif pmap[sy+1][sx]== 'L':
    r1y+=1
    pmap[r1y][r1x] = '╚'
elif pmap[sy+1][sx] == '|':
    r1y+=1
    pmap[r1y][r1x] = '║'
elif pmap[sy][sx-1]== 'F':
    r1x-=1
    pmap[r1y][r1x] = '╔'
elif pmap[sy][sx-1]== 'L':
    r1x-=1
    pmap[r1y][r1x] = '╚'
elif pmap[sy][sx-1] == '-':
    r1x-=1
    pmap[r1y][r1x] = '═'
elif pmap[sy][sx+1]== 'J':
    r1x+=1
    pmap[r1y][r1x] = '╝'
elif pmap[sy][sx+1]== '7':
    r1x+=1
    pmap[r1y][r1x] = '╗'
elif pmap[sy][sx+1] == '-':
    r1x+=1
    pmap[r1y][r1x] = '═'
r1count+=1
r2y=sy
r2x=sx
r2count = 0
if (pmap[sy-1][sx]== 'F' or pmap[sy-1][sx]== '7' or pmap[sy-1][sx] == '|') and sy-1 !=r1y:
    r2y-=1
elif (pmap[sy+1][sx]== 'J' or pmap[sy+1][sx]== 'L' or pmap[sy+1][sx] == '|') and sy+1 !=r1y:
    r2y+=1
elif (pmap[sy][sx-1]== 'F' or pmap[sy][sx-1]== 'L' or pmap[sy][sx-1] == '-') and sx-1 !=r1x:
    r2x-=1
else:
    r2x+=1

ltoblock(pmap,r2x,r2y)

r2count+=1
while r1x!=r2x or r1y!=r2y:
    z = progress(pmap,r1x,r1y)
    r1x = int(z.real)
    r1y = int(z.imag)
    r1count+=1
    z = progress(pmap,r2x,r2y)
    r2x = int(z.real)
    r2y = int(z.imag)
    r2count+=1
    if testend(pmap,r1x,r2x,r1y,r2y):
        break
print(r1count)
