N, M = map(int, input().split())
list = [0] * (M + 2)
sum = 0

for _ in range(0, N):
    l, r, s = map(int, input().split())
    list[l] += s
    list[r + 1] -= s
    sum += s

for i in range(0, M + 1):
    list[i + 1] += list[i]

min = list[1]
for i in range(2, M + 1):
    min = list[i] if min > list[i] else min

print(sum - min)