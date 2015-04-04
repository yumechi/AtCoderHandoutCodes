N, K = map(int, input().split())
tlist = [int(input()) for _ in range(N)]
for i in range(3, N):
    if sum(tlist[i-3:i]) < K:
        print(i)
        exit(0)
print("-1")