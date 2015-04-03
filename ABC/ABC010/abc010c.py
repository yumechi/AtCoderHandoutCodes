import math

xta, yta, xtb, ytb, T, V = map(int, input().split())
n = int(input())
f = lambda x1, x2, y1, y2: pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2)
distance = lambda x1, x2, y1, y2: math.sqrt(f(x1, x2, y1, y2))
for _ in range(0, n):
    x, y = map(int, input().split())
    if distance(xta, x, yta, y) + distance(xtb, x, ytb, y) <= T * V:
        print("YES")
        break
else:
    print("NO")