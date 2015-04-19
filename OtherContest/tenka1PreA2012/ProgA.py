N = int(input())
table = [1 for _ in range(N + 3)]
for i in range(N):
    table[i + 2] = table[i+1] + table[i]
print(table[N])
