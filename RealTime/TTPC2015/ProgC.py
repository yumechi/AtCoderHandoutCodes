s = input()
o = "oookayama"
while o in s:
    fidx = s.index(o)
    lidx = fidx + len(o)
    while fidx >= 0:
        if s[fidx] != "o":
            break
        else:
            fidx -= 1
    fidx += 1
    t = s[fidx:lidx]
    while "oo" in t:
        if "oo" in t:
            tfidx = t.index("oo")
            t = t[:tfidx] + "O" + t[tfidx+2:]
        if "OO" in t:
            tfidx = t.index("OO")
            t = t[:tfidx] + "o" + t[tfidx+2:]
    s = s[:fidx] + t + s[lidx:]
print(s)
