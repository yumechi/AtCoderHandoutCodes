def ckeck(list):
    for i in range(N):
        for j in range(i, N):
            zeroCount = list[i:j + 1].count("0")
            oneCount = list[i:j + 1].count("1")
            if abs(zeroCount - oneCount) > K:
                return 0
    return 1
 
N, K = map(int, input().split())
S = input()
res = 0
MODNUM = 1000000007
 
hatenaCounts = S.count("?")
if hatenaCounts == 0:
    res += ckeck(list(S))
else:
    counter = 2 ** hatenaCounts - 1
    while counter >= 0:
        tc = counter
        ts = list(S)
        for i in range(N):
            if ts[i] == "?":
                t = tc & 1
                tc >>= 1
                ts[i] = str(t)
        res += ckeck(ts)
        counter -= 1
 
print(res % MODNUM)