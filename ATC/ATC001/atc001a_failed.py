import sys

mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
ngXRange = lambda x: not (0 <= x < W)
ngYRange = lambda y: not (0 <= y < H)
 
def dfs(y, x):
    if ngXRange(x) or ngYRange(y) or table[y][x] == "#":
        return
    if visited[y][x]:
        return
   
    visited[y][x] = True
    for i in range(4):
        ny = y + my[i]
        nx = x + mx[i]
        dfs(ny, nx)

H, W = map(int, input().split())
table = [input() for _ in range(H)]
visited = [[False for _ in range(W)]for _ in range(H)]
sx, sy = 0, 0
gx, gy = 0, 0
sys.setrecursionlimit(10000000)
for i in range(H):
    for j in range(W):
        if table[i][j] == "s":
            sx, sy = j, i
        if table[i][j] == "g":
            gx, gy = j, i
dfs(sy, sx)
print("Yes" if visited[gy][gx] else "No")
