def solve1(n, k, al):
    answer = 0
    start = max(0, n - 2 * k)
    lans = sum(al[:start])
    kans = sum(al[start:start + k])
    ans = 0
    for i in range(0, 2 * k):
        end = start + i + k
        print("F", start + i, end, kans, lans, ans)
        if end >= n:
            break
        ans = max(lans + kans, lans)
        kans += al[end] - al[start + i]
        if start + i < n - k and al[start + i] > 0:
            lans += al[start + i]
        print("E", start + i, end, kans, lans, ans)
    answer = max(answer, ans)

    al = al[::-1]
    lans = sum(al[:start])
    kans = sum(al[start:start + k])
    ans = 0
    for i in range(0, 2 * k):
        end = start + k + i
        print("F", start + i, end, kans, lans, ans)
        if end >= n:
            break
        ans = max(lans + kans, lans)
        kans += al[end] - al[start + i]
        if start + i < n - k and al[start + i] > 0:
            lans += al[start + i]
        print("E", start + i, end, kans, lans, ans)
    answer = max(answer, ans)
    print(answer)

def solve2(n, k, al):
    pass

def solve():
    n, k = map(int, input().split())
    al = [int(i) for i in input().split()]

    solve1(n, k, al)
    """
    if(n < 2 * k):
        solve1(n, k, al)
    else:
        solve2(n, k, al)
    """

if __name__=="__main__":
    solve()