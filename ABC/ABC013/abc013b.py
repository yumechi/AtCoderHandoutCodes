d = abs(int(input()) - int(input()))
print(min(d, 10 - d))

"""
# ループ使うバージョン
a = int(input())
b = int(input())
dcount = 0
ta = a
tb = b
while ta != tb:
    ta += 1
    ta %= 10
    dcount += 1

ta = a
tb = b
ucount = 0
while ta != tb:
    ta += 9 if ta == 0 else -1
    ucount += 1

print(min(dcount, ucount))
"""
