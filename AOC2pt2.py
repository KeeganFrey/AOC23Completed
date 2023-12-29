import re

filepath = "input2.txt"
with open(filepath,'r') as file:
    lines = file.readlines()
file.close()
count = 0
sum = 0
rmin = 0
bmin = 0
gmin = 0
num = 0
for item in lines:
    seperated = re.split(r'[ :,;\n]',item)
    seperated = [item for item in seperated if item != ""]
    flag = False
    npflag = False
    for items in seperated:
        if flag:
            if items == "red" and num > rmin:
                rmin = num
            elif items == "blue" and num > bmin:
                bmin = num
            elif items == "green" and num > gmin:
                gmin = num
            
            flag = False
        if items.isdigit():
            flag = (count != 1)
            num = int(items)
        count +=1

    sum += rmin*bmin*gmin
    rmin = 0
    gmin = 0
    bmin= 0
    count = 0

print(sum)