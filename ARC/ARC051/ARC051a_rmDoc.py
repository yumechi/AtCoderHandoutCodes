def calcDistance(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    return pow(x ** 2 + y ** 2, 0.5)

def inCircle(cx, cy, r, x, y):
    return calcDistance(cx, cy, x, y) <= r

def inRectangle(rx1, ry1, rx2, ry2, x, y):
    if rx1 == rx2 or ry1 == ry2:
        # 未チェック
        import sys
        sys.stderr.write("長方形の座標値がおかしいです")
        print(" ".join(["rx1", "rx2", "ry1", "ry2"]))
        print(" ".join([str(i) for i in [rx1, rx2, ry1, ry2]]))
        raise Exception

    # 大きさチェック
    if rx2 < rx1:
        rx1, rx2 = rx2, rx1
    if ry2 < ry1:
        ry1, ry2 = ry2, ry1
    return rx1 <= x <= rx2 and ry1 <= y <= ry2

def circleInRectangle(cx, cy, r, rx1, ry1, rx2, ry2):
    l1 = [-1, 1, -1, 1]
    l2 = [1, 1, -1, -1]
    cnt = 0
    for i in range(4):
        if(inRectangle(rx1, ry1, rx2, ry2, (cx + r * l1[i]), (cy + r * l2[i]))):
            cnt += 1
    return cnt == 4

def rectangleInCircle(rx1, ry1, rx2, ry2, cx, cy, r):
    l1 = [rx1, rx2, rx1, rx2]
    l2 = [ry1, ry1, ry2, ry2]
    cnt = 0
    for i in range(4):
        if(inCircle(cx, cy, r, l1[i], l2[i])):
            cnt += 1
    return cnt == 4

def solve():
    cx, cy, r = map(int, input().split())
    rx1, ry1, rx2, ry2 = map(int, input().split())
    # RED:CIRCLE
    print("NO" if circleInRectangle(cx, cy, r, rx1, ry1, rx2, ry2) else "YES")
    # BLUE:RECTANGLE
    print("NO" if rectangleInCircle(rx1, ry1, rx2, ry2, cx, cy, r) else "YES")

if __name__=="__main__":
    solve()