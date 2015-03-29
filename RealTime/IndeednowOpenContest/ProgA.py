N = int(input())
list = list(map(int, input().split()))
list.sort()
maxnum = 0
minnum = 9999
length = len(list) - 1
for i in range(0, int(N / 2)):
    maxnum = max(maxnum, list[i] + list[length - i])
    minnum = min(minnum, list[i] + list[length - i])
print(int(maxnum - minnum))