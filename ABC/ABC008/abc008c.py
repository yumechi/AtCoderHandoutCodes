import itertools

N = int(input())
coins = [int(input()) for _ in range(N)]
per = 0
for i in range(N):
    s = 0
    for j in range(N):
        if i != j and coins[i] % coins[j] == 0:
            s += 1
    if s == 0:
        per += 1.0
    elif s % 2 == 1:
        per += 0.5
    else:
        per += ((s / 2) + 1) / (s + 1)
print(per)