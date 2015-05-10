def clachashnum(s):
    ret = 0
    for c in s:
        ret += ord(c) - ord("a") + 1
    return ret
 
s = input()
hashnum = clachashnum(s)
if not 2 <= hashnum <= 519:
    print("NO")
else:
    res = ""
    if hashnum >= 27:
        while hashnum >= 26:
            res += "z"
            hashnum -= 26
        res += chr(ord("a") + hashnum - 1)
        if s == res:
            res = res[::-1]
    else:
        # 1 alpha
        if len(s) == 1:
            res = chr(ord("a") + hashnum - 2) + "a"
        else:
            res = chr(ord("a") + hashnum - 1)
        
    print(res if clachashnum(s) == clachashnum(res) else "NO")