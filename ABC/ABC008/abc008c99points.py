import itertools

N = int(input())
coins = [int(input()) for _ in range(N)]
total = 0
for coin in itertools.permutations(coins):
    checklist = [True] * N
    for i in range(0, N):
        for j in range(i + 1, N):
            if coin[j] % coin[i] == 0:
                checklist[j] = not checklist[j]
    for i in range(N):
        if checklist[i]:
            total += 1

combi = 1
for i in range(1, N + 1):
    combi *= i

print(total / combi)