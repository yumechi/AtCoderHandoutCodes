N, T = map(int, input().split())
pli = list(map(int, input().split()))
sli = [list(map(int, input().split())) for _ in range(N)]
tli = [list(map(int, input().split())) for _ in range(N)]
indexs = [0 for _ in range(N)]
 
while T > 0:
    minscore = 10001
    mini = None
    for i in range(N):
        s, index = sli[i], indexs[i]
        if pli[i] > index and minscore > s[index]:
            minscore = s[index]
            mini = i
    
    if mini == None:
        break
    loss = tli[mini][indexs[mini]]
    T -= loss
    if T >= 0:
        indexs[mini] += 1
 
res = 0
for (s, i) in zip(sli, indexs):
    res += s[i - 1] if i > 0 else 0
    
print(res)