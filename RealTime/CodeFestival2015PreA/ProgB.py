n = int(input())
l = list(map(int, input().split()))
res = 0
for i in range(n):
    res += l[i] * (2 ** (n-i-1))
print(res)
