def solve():
    w, h, n = [int(i) for i in input().split()]
    dic = dict()
    for i in range(n):
        a, b = map(lambda x: int(x) - 1, input().split())
        for j in range(3):
            for k in range(3):
                aj = a + j - 1
                bk = b + k - 1
                if 0 < aj and aj < w - 1 and 0 < bk and bk < h - 1:
                    if (aj, bk) in dic:
                        dic[(aj, bk)] += 1
                    else:
                        dic[(aj, bk)] = 1
    ans = [0 for i in range(10)]
    for v in dic.values():
        ans[v] += 1
    for i in range(10):
        if i == 0:
            print((w - 2) * (h - 2) - sum(ans))
        else:
            print(ans[i])
 
 
if __name__=="__main__":
    solve()
