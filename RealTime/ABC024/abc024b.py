N, T = map(int, input().split())
ali = [int(input()) for _ in range(N)]
res = T
before = ali[0]
for i in range(1, N):
    if before + T > ali[i]:
        res += (ali[i] - ali[i-1])
    else:
        res += T
    before = ali[i]
print(res)
