# python is not suitable DP problems
# C++ can pass the test using same algorythm
import sys

n, p = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])
data.sort(reverse=True)

dp = [0 for _ in range(p+5)]
res = 0
for i in range(n):
    f, s = data[i]
    for j in range(p)[::-1]:
        cur = j + f
        if cur <= p:
            dp[cur] = max(dp[cur], s + dp[j])

    if i < n-1:
        res = max(res, dp[p] + data[i+1][1])

print(max(res, dp[p]))
