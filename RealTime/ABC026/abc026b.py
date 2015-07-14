import math
 
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
li = li[::-1]
rsum = 0
for i in range(n):
    if i % 2 == 0:
        rsum += li[i] ** 2
    else:
        rsum -= li[i] ** 2
print(rsum * math.pi)