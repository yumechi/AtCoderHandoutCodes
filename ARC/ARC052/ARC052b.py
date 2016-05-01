import math

def solve():
    n, q = map(int, input().split())
    al = [[] for _ in range(n)]
    calcV = lambda r, h: ((math.pi) * (r ** 2) * h) / 3
    for i in range(n):
        x, r, h = map(int, input().split())
        al[i] = [x, r, h, calcV(r, h), x + h, calcV(r, h) / h ** 3]

    for i in range(q):
        a, b = map(int, input().split())
        res = 0.0
        for e in al:
            # 処理しない
            if b <= e[0] or e[4] <= a:
                continue

            if a <= e[0] < e[4] <= b:
                res += e[3]
            elif a <= e[0] <= b <= e[4]:
                t = e[4] - b
                res += e[3] - (t ** 3) * e[5]
            elif e[0] <= a <= e[4] <= b:
                t = e[4] - a
                res += (t ** 3) * e[5]
            elif e[0] <= a < b <= e[4]:
                tres = 0.0
                t = e[4] - a
                tres += (t ** 3) * e[5]
                t1 = e[4] - b
                tres -= (t1 ** 3) * e[5]
                res += tres
        print(res)

if __name__=="__main__":
    solve()