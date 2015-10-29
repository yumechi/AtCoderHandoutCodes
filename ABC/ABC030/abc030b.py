h, m = map(int, input().split())
res = abs(360 * (h % 12 + m / 60) / 12 - 360 * (m / 60))
print(res if res <= 180 else 360 - res)
