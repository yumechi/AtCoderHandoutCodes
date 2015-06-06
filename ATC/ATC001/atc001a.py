import sys
import collections

H, W = map(int,sys.stdin.readline().split())
table = [list(row.rstrip("\n")) for row in sys.stdin.readlines()]
deq = collections.deque()
for i in range(H):
    for j in range(W):
        if table[i][j] == "s":
            deq.append((i, j))
            break

while len(deq) > 0:
    y, x = deq.popleft()
    if y < 0 or H <= y or x < 0 or W <= x or table[y][x] == "#":
        continue
    if table[y][x] == "g":
        print("Yes")
        break

    table[y][x] = "#"
    for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
        deq.append((ny, nx))
else:
    print("No")
