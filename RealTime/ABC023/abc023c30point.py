R, C, K = map(int, input().split())
N = int(input())
candies = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
 
rows = dict(zip(range(0, R), [0 for _ in range(R)]))
cols = dict(zip(range(0, C), [0 for _ in range(C)]))
for i in range(N):
    rows[candies[i][0]] += 1
    cols[candies[i][1]] += 1
 
res = 0
for i in range(R):
    if rows[i] > K:
        continue
    for j in range(C):
        t = rows[i] + cols[j]
        t -= 1 if [i, j] in candies else 0
        if t == K:
            res += 1
 
print(res)