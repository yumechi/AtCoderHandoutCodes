n = int(input())
res = 0
for i in range(n):
    res = max(res, (n - i) * i)
print(res)