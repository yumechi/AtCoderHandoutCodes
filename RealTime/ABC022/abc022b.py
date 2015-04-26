N = int(input())
table = [0 for _ in range(100001)]
for _ in range(N):
    i = int(input())
    table[i] += 1
res = 0
for i in range(100001):
    if table[i] > 1:
        res += table[i] - 1
print(res)