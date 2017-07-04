def solve():
    n, k = map(int, input().split())
    al = [int(c) - 1 for c in input().split()]
    sl = [input() for _ in range(n)]

    # 全部出す場合は空行だけでおしまい
    if n == k:
        print()
        return

    newlist = []
    minword = "otaku" * 100000
    for i in range(n):
        if i in al:
            newlist.append((sl[i], True))
            if len(sl[i]) < len(minword):
                minword = sl[i]
        else:
            newlist.append((sl[i], False))

    wordindex = 0
    ans = ""
    while wordindex < len(minword):
        ans += minword[wordindex]
        for item in newlist:
            if item[1]:
                if item[0].find(ans) != 0:
                    print(-1)
                    return
            else:
                if item[0].find(ans) == 0:
                    break
        else:
            print(ans)
            return
        wordindex += 1
    print(-1)

if __name__=="__main__":
    solve()
