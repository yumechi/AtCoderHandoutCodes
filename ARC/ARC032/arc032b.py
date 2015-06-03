import sys
 
def find(x):
    if x == table[x]:
        return x
    else:
        table[x] = find(table[x])
        return table[x]
 
def union(x, y):
    s1 = find(x)
    s2 = find(y)
    if s1 != s2:
        table[s2] = s1
 
N, M = map(int, input().split())
table = [i for i in range(N)]
sys.setrecursionlimit(100001)
for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    union(a, b)
 
res = 0
for i in range(N):
    if table[i] == i:
        res += 1
print(res - 1)
