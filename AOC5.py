import re

def maptransform(inlist, outlist, map):
    for item in inlist:
        maps = len(map)/3
        i=0
        nts = True
        while i<maps:
            if map[i*3+1]+map[i*3+2]>item and item >= map[i*3+1]:
                outlist.append(item-map[i*3+1]+map[i*3])
                nts = False
            i+=1
        if nts:
            outlist.append(item)

filepath = "input5.txt"
with open(filepath,'r') as file:
    lines = file.readlines()
seeds = []
sts = []
stf = []
ftw = []
wtl = []
ltt = []
tth = []
htl = []
mrt = ""
for item in lines:
    seperated = re.split(r'[ \n]', item)
    seperated = [item for item in seperated if item != ""]
    for text in seperated:
        if text.isdigit():
            #Add to the int maps corresponding to the text
            if mrt == "seeds:":
                seeds.append(int(text))
            elif mrt == "seed-to-soil":
                sts.append(int(text))
            elif mrt == "soil-to-fertilizer":
                stf.append(int(text))
            elif mrt == "fertilizer-to-water":
                ftw.append(int(text))
            elif mrt == "water-to-light":
                wtl.append(int(text))
            elif mrt == "light-to-temperature":
                ltt.append(int(text))
            elif mrt == "temperature-to-humidity":
                tth.append(int(text))
            elif mrt == "humidity-to-location":
                htl.append(int(text))
        else:
            if text != "map:":
                mrt = text

soil = []
maptransform(seeds,soil,sts)
fert = []
maptransform(soil,fert,stf)
water = []
maptransform(fert,water,ftw)
light = []
maptransform(water,light,wtl)
temp = []
maptransform(light,temp,ltt)
humid = []
maptransform(temp,humid,tth)
loc = []
maptransform(humid,loc,htl)

print(min(loc))
