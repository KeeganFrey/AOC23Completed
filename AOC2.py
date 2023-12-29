import re

filepath = "input2.txt"
with open(filepath,'r') as file:
    lines = file.readlines()
file.close()
count = 0
sum = 0
for item in lines:
    seperated = re.split(r'[ :,;\n]',item)
    seperated = [item for item in seperated if item != ""]
    flag = False
    npflag = False
    digit = 0
    for items in seperated:
        if flag:
            if digit > 14:
                npflag = True
            elif digit == 14 and items != "blue":
                npflag = True
            elif digit == 13 and items == "red":
                npflag = True
            
            flag = False
        if items.isdigit():
            flag = (count != 1)
            digit = int(items)
        count +=1
    
    if not npflag:
        sum += int(seperated[1])
    else:
        npflag = False
    count = 0

print(sum)