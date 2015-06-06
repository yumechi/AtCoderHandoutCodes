N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]
 
unilist = [i for i in range(N)]

def find(x):
    if x == unilist[x]:
        return x
    else:
        unilist[x] = find(unilist[x])
        return unilist[x]

def union(x, y):
    s1, s2 = find(x), find(y)
    if s1 != s2:
        unilist[s2] = s1

def isSame(x, y):
    return find(x) == find(y)

for query in queries:
    if query[0] == 0:
        union(query[1], query[2])
    else:
        print("Yes" if isSame(query[1], query[2]) else "No")
