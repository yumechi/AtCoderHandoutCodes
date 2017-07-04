def solve():
    ia, oa, ta, ja, la, sa, za = map(int, input().split())
    ans = 0
    ans += oa
    ans += ia // 2 * 2
    minjl = min(ja, la)
    ans += minjl * 2
    if ia % 2 == 1 and minjl > 0:
        ans += 1
    print(ans)

if __name__=="__main__":
    solve()