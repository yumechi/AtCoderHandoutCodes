N, va, vb, L = map(int, input().split())
for _ in range(N):
    second = L / va
    L = vb * second
print("%lf" % L)