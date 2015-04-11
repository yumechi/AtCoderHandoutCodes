# from my smartphone
import math
 
N = int(input())
pointlist = []
for _ in range(N):
    x, y = map(int, input().split())
    pointlist.append([x, y])
 
maxlength = 0
for i in range(N - 1):
    first = pointlist[i]
    for j in range(i + 1, N):
        second = pointlist[j]
        tlength = math.sqrt(abs(first[0] - second[0]) ** 2 + abs(first[1] - second[1]) ** 2)
        maxlength = max(maxlength, tlength)
 
print(maxlength)