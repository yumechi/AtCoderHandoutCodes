a, b, c = map(int, input().split())
N = int(input())
oriA, oriB, oriC = a, b, c
for _ in range(N):
    if a < N:
        a += 1
    if b < N * 2:
        b += 2
        if b > N * 2:
            b -= b % 2
    if c < N * 3:
        c += 3
        if c > N * 3:
            c -= c % 3
print(a - oriA, b - oriB, c - oriC)