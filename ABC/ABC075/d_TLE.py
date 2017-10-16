from itertools import permutations

def solve():
    n, k = map(int, input().split())
    xs, ys = [], [] 
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    rsxs = sorted(xs)[::-1]
    rsys = sorted(ys)[::-1]
    dxs = dict()
    dys = dict()
    for i in range(n):
        dxs[xs[i]] = [n - rsxs.index(xs[i]), xs.count(xs[i])]
        dys[ys[i]] = [n - rsys.index(ys[i]), ys.count(ys[i])]

    ans = ((10 ** 9) * (10 ** 9)) ** 2
    xss, yss = set(xs), set(ys)
    for x1 in xss:
        for x2 in xss:
            if x1 == x2:
                continue
            for y1 in yss:
                for y2 in yss:
                    if y1 == y2:
                        continue
                    minX, maxX = sorted([x1, x2])
                    minY, maxY = sorted([y1, y2])
                    cnt = ((dxs[maxX][0] - dxs[minX][0] + dxs[minX][1]) + (dys[maxY][0] - dys[minY][0] + dys[minY][1])) // 2
                    if cnt >= k:
                        print(cnt, minX, maxX, minY, maxY, (maxX - minX) * (maxY - minY))
                        ans = min(ans, (maxX - minX) * (maxY - minY))
    print(ans)

if __name__=="__main__":
    solve()
