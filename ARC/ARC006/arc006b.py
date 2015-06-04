N, L = map(int, input().split())
lines  = list(reversed([input() for _ in range(L)]))
maru = input()
maruidx = maru.find("o")
for i in range(L):
    if maruidx > 0 and lines[i][maruidx-1] == "-":
        maruidx -= 2
    elif maruidx < (N-1)*2 and lines[i][maruidx+1] == "-":
        maruidx += 2
print(maruidx // 2 + 1)
