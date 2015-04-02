N = int(input())
table = [list(map(int, input().split())) for _ in range(0, N)]
coming = [0] * (N * 2 + 1)
for S, T in table:
    coming[S] += 1

for i in range(0, N * 2):
    coming[i + 1] += coming[i]

for i in range(0, N):
    S, T = table[i]
    print(coming[T] - coming[S])