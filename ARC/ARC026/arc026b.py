from math import sqrt

N = int(input())
res = 0
for i in range(1, int(sqrt(N)) + 1):
    if N % i == 0:
        res += i if N == i * i or i == 1 else i + N // i

print("Deficient" if N > res or N == 1 else "Abundant" if N < res else "Perfect")