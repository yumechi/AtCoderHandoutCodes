import math

N = int(input())
alist = list(map(int, input().split()))
while 0 in alist:
    alist.remove(0)

print(math.ceil(sum(alist) / len(alist)))