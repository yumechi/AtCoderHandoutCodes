N = int(input())
hlist = [int(input()) for _ in range(N)]

if N == 1:
    print(1)
    exit(0)

flag = True if hlist[0] > hlist[1] else False
maxnum = 0
start = 0

for i in range(1, N):
    if flag:
        if hlist[i - 1] > hlist[i]:
            flag = not flag
    else:
        if hlist[i - 1] < hlist[i]:
            maxnum = max(maxnum, i - start)
            flag = not flag
            start = i - 1

maxnum = max(maxnum, (N - 1) - start + 1)

print(maxnum)