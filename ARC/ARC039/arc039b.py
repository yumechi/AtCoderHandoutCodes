from functools import reduce
from operator import mul

N, K = map(int, input().split())
combi = lambda i, j: reduce(mul, range(i, i - j, -1)) // reduce(mul, range(j, 0, -1)) if j > 0 else 1

res = combi(N + K - 1, K) if N > K else combi(N, K % N)
print(res % 1000000007)
