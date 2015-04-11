# TLE してしまう，探索を改善しなければ…
MOD = 1000000007
N = int(input())
start, end = map(int, input().split())
M = int(input())
table = []
for _ in range(M):
    x, y = map(int, input().split())
    table.append([x, y])

que = []
checked = []
que.append([start, 0])
counter = 0
goalpath = 0
while True:
    if len(que) < 1:
        break
    current = que.pop(0)
    if current[1] > goalpath > 0:
        break
    for i in range(M):
        if not (table[i][1] in checked) and table[i][0] == current[0]:
            if table[i][1] == end and (goalpath == 0 or current[1] == goalpath):
                counter += 1
            elif goalpath == 0:
                que.append([table[i][1], current[1] + 1])
        if not (table[i][0] in checked) and table[i][1] == current[0]:
            if table[i][0] == end and (goalpath == 0 or current[1] == goalpath):
                counter += 1
            elif goalpath == 0:
                que.append([table[i][0], current[1] + 1])
    if counter > 0 and goalpath == 0:
        goalpath = current[1]
    checked.append(current[0])
print(counter % MOD)