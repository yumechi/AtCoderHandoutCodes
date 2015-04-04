R, C = map(int, input().split())
start = list(map(int, input().split()))
goal = list(map(int, input().split()))

for i in range(2):
    start[i] -= 1
    goal[i] -= 1

maptable = [list(str(input())) for x in range(R)]

que = [[start]]
# up, down, right, left
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

count = 0
maptable[start[0]][start[1]] = '{0}'.format(count)
while True:
    if len(que) == 0:
        exit(1)

    current = que.pop(0)
    count += 1
    nextsearch = []

    for c in current:
        for i in range(4):
            ny = c[0] + my[i]
            nx = c[1] + mx[i]
            # find out
            if ny == goal[0] and nx == goal[1]:
                print(count)
                exit(0)

            if maptable[ny][nx] == '.':
                nextsearch.append([ny, nx])
                maptable[ny][nx] = '{0}'.format(count)

    que.append(nextsearch)