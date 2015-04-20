import math as m
N = int(input())
sum = 0
tax = 1.05
for _ in range(N):
    a, b = map(int, input().split())
    sum += a * b
print(m.floor(sum * tax))