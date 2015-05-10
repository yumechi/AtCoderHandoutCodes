N, T, E = map(int, input().split())
xli = list(map(int, input().split()))
res = -1
 
for i in range(N):
    for time in range(T - E, T + E + 1):
        if time % xli[i] == 0:
            res = i + 1
            break
    if res != -1:
        break
 
print(res)