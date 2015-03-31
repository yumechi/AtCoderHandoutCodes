N = int(input())
a, b, c = 0, 0, 1
if N < 3:
    c = 0
else:
    for _ in range(0, N - 3):
        a, b, c = b, c, (a + b + c) % 10007
print(c % 10007)