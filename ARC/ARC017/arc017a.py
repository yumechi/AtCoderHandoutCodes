import math as m
N = int(input())
for i in range(2, int(m.sqrt(N)) + 1):
    if N % i == 0:
        print("NO")
        break
else:
    print("YES")