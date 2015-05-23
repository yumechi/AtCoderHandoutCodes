import copy

N, D, K = map(int, input().split())
movelist = [list(map(int, input().split())) for _ in range(D)]
goallist = [list(map(int, input().split())) for _ in range(K)]
goalday = [0 for _ in range(K)]
day = 0
for m in movelist:
    li = []
    for i in range(len(goallist)):
        if goallist[i][0] < goallist[i][1] and m[0] <= goallist[i][0] < m[1]:
            if goallist[i][1] <= m[1]:
                goallist[i][0] = goallist[i][1]
                li.append(i)
            else:
                goallist[i][0] = m[1]
        elif goallist[i][0] > goallist[i][1] and m[0] < goallist[i][0] <= m[1]:
            if m[0] <= goallist[i][1]:
                goallist[i][0] = goallist[i][1]
                li.append(i)
            else:
                goallist[i][0] = m[0]
    day += 1
    for i in li:
        goalday[i] = str(day)
    if 0 not in goalday:
        break

print("\n".join(goalday))