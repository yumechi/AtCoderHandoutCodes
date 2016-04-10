def solve():
    n = int(input())
    al = [int(input()) for _ in range(n)]
    al2 = list(set(al))
    al2.sort()
    al2len = len(al2)
    am = dict(zip(al2, [i for i in range(al2len)]))
    for e in al:
        print(am[e])

if __name__=="__main__":
    solve()