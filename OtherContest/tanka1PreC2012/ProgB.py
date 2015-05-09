def setdic(dic, st):
     if st in dic:
         dic[st] += 1
 
def dicnum(dic):
     count = 0
     incheck = 0
     for k in dic.values():
          if k > 0:
              count += 1
              incheck += 1
     return True if incheck == 5 and count >= 5 else False
 
s = input().replace("10", "T")
sli = [s[i:i+2] for i in range(0, len(s), 2)]
srfc = {"ST":0, "SJ":0, "SQ":0, "SK":0, "SA":0}
hrfc = {"HT":0, "HJ":0, "HQ":0, "HK":0, "HA":0}
drfc = {"DT":0, "DJ":0, "DQ":0, "DK":0, "DA":0}
crfc = {"CT":0, "CJ":0, "CQ":0, "CK":0, "CA":0}
dics = [srfc, hrfc, drfc, crfc]
okdic = None
junk = []
 
for st in sli:
    junk.append(st)
    for d in dics:
        setdic(d, st)
        if dicnum(d):
            okdic = d
    
    if okdic != None:
        break
 
for k in okdic.keys():
    junk.remove(k)
 
print("0" if len(junk) == 0 else "".join(junk).replace("T", "10"))