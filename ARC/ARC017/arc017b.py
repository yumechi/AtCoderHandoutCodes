N, K = map(int, input().split())
if K == 1:
    print(N)
    exit(0)

table = [int(input()) for _ in range(N)]
res = 0
cont = 0
for i in range(N - 1):
    if table[i+1] > table[i]:
        cont += 1
        if cont >= (K - 1):
            res += 1
    else:
        cont = 0
print(res)
