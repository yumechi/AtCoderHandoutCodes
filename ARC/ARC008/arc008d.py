N, M = map(int, input().split())
maxnum = minnum = 1
table = [[1.0, 0.0] for _ in range(0, N)]
result = [1.0] * N
for _ in range(0, M):
    p, a, b = map(float, input().split())
    p = int(p)
    table[p - 1][0] = a
    table[p - 1][1] = b
    for i in range(p - 1, N - 1):
        result[i + 1] = table[i][0] * result[i] + table[i][1]
    maxnum = max(result[N - 1], maxnum)
    minnum = min(result[N - 1], minnum)
 
print(minnum)
print(maxnum)