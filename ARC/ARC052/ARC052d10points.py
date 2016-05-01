def solve():
    k, m = map(int, input().split())
    res = 0
    for i in range(1, m+1):
        if i % k == sum(map(int, list(str(i)))) % k:
            res += 1
    print(res)


if __name__=="__main__":
    solve()
