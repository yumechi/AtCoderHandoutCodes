n = int(input())
table = list(map(int, input().split()))
table.sort()
table = table[::-1]
res = 0
for i in range(n):
    if i % 2 == 0:
        res += table[i]
print(res)