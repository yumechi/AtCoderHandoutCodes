def dfs(current, prev, checked):
    gcheck.update([current])
    if current in checked:
        return False
    for x, y in table:
        if x == current and not (y == prev):
            now, pv = y, x
            checked.append(x)
            if not dfs(now, pv, checked):
                return False
            checked.remove(x)
        if y == current and not (x == prev):
            now, pv = x, y
            checked.append(y)
            if not dfs(now, pv, checked):
                return False
            checked.remove(y)
    return True

N, M = map(int, input().split())
table = []
gcheck = set([])
usednum = set([])
for _ in range(M):
    x, y = map(int, input().split())
    table.append([x, y])
    usednum.update([x, y])

res = 0
for i in range(1, N + 1):
    if not(i in gcheck):
        if dfs(i, 0, []):
            res += 1

print(res)