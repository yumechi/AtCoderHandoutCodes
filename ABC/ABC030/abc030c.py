import bisect
N, M = map(int, input().split())
X, Y = map(int, input().split())
ali = [int(i) for i in input().split()]
bli = [int(i) for i in input().split()]
res, idx = 0, 0
func = lambda li, i: bisect.bisect_left(li, i)
while True:
    if idx >= N:
        break
    idx = func(bli, ali[idx] + X)
    if idx >= M:
        break
    idx = func(ali, bli[idx] + Y)
    res += 1
print(res)
