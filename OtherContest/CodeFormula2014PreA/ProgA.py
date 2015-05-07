import math

n = int(input())
for i in range(int(math.pow(n, 1.0 / 3.0)) + 2):
    if i ** 3 == n:
        print("YES")
        break
else:
    print("NO")
