# まったく溶けてない  動かない

H, W, T = map(int, input().split())
tablelist = []
for _ in range(0, H):
    tablelist.append(input())

startpoint = []
currentpoint = []
endpoint = []
tablepoint = [[0 for _ in range(0, W)] for _ in range(0, H)]
for i in range(0, H):
    for j, c in enumerate(tablelist[i]):
        if c == "S":
            startpoint = [i, j]
            currentpoint = [i, j]
            tablepoint[i][j] = 0
        elif c == "G":
            endpoint = [i, j]
            tablepoint[i][j] = 1
        elif c == ".":
            tablepoint[i][j] = 1
        elif c == "#":
            tablepoint[i][j] = -1

