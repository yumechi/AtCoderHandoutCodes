def solve():
    rowstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    h, w = map(int, input().split())
    snaketable = [input().split() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if "snuke" in snaketable[i][j]:
                print("{0}{1}".format(rowstr[j], i+1))
                return


if __name__=="__main__":
    solve()