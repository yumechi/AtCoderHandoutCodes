def calcDistance(x1, y1, x2, y2):
    """
    二点間の距離を計算する
    @author yumechi
    @param  x1      点1のx座標
    @param  y1      点1のy座標
    @param  x2      点2のx座標
    @param  y2      点2のy座標
    """
    x = x1 - x2
    y = y1 - y2
    return (x ** 2 + y ** 2) ** 0.5

def inCircle(cx, cy, r, x, y):
    """
    その点が円の中にあるかどうかを判定する
    @author yumechi
    @param  cx      円の中心のx座標
    @param  cy      円の中心のy座標
    @param  r       円の半径
    @param  x       点のx座標
    @param  y       点のy座標
    """
    return calcDistance(cx, cy, x, y) <= r

def inRectangle(rx1, ry1, rx2, ry2, x, y):
    """
    その点が長方形の中にあるかどうかを判定する
    @author yumechi
    @param  rx1      長方形のx座標
    @param  ry1      長方形のy座標
    @param  rx2      長方形のx座標（rx1 < rx2)
    @param  ry2      長方形のy座標 (ry1 < ry2)
    @param  x        点のx座標
    @param  y        点のy座標
    """
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
    """
    円が長方形の中にあるかどうかを判定する
    @author yumechi
    @param  cx       円の中心のx座標
    @param  cy       円の中心のy座標
    @param  r        円の半径
    @param  rx1      長方形のx座標1
    @param  ry1      長方形のy座標1
    @param  rx2      長方形のx座標2
    @param  ry2      長方形のy座標2
    """
    l1 = [-1, 1, -1, 1]
    l2 = [1, 1, -1, -1]
    cnt = 0
    for i in range(4):
        if(inRectangle(rx1, ry1, rx2, ry2, (cx + r * l1[i]), (cy + r * l2[i]))):
            cnt += 1
    return cnt == 4

def rectangleInCircle(rx1, ry1, rx2, ry2, cx, cy, r):
    """
    長方形が円の中にあるかどうかを判定する
    @author yumechi
    @param  rx1      長方形のx座標1
    @param  ry1      長方形のy座標1
    @param  rx2      長方形のx座標2
    @param  ry2      長方形のy座標2
    @param  cx       円の中心のx座標
    @param  cy       円の中心のy座標
    @param  r        円の半径
    """
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