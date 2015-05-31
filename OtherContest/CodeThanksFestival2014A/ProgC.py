N, M = map(int, input().split())
Pli = list(map(int, input().split()))
res = 0
for t in map(int, input().split()):
    res += Pli[t-1]
print(res)
