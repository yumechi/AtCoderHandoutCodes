import math

a, b, c = map(int, input().split())
ft, low, high = 100, 0, 500
calc = lambda m: a * m + b * math.sin(c * m * math.pi)
for i in range(100):
    mid = (low + high) / 2
    current = calc(mid)
    if current < ft:
        low = mid
    else:
        high = mid
print((low + high) / 2)
