N = int(input())

li = [False for _ in range(10 ** 100 + 1)]
res = [0 for _ in range(N)]
for i in range(N):
    counter = 0
    s, c = map(int, input().split())
    while c > counter:
        if not li[s]:
            counter += 1
            li[s] = True
        else:
            s += 1
    res[i] = s

for i in res:
    print(i)
