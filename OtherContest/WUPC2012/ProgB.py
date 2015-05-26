N = int(input())
li = [input() for _ in range(N)]
table = []
for i in range(N):
    for j in range(N):
        if i != j:
            table.append(li[i] + li[j])
res = sorted(table)
print(res[0])
