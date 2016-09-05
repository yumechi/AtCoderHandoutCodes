def solve():
    n, x = map(int, input().split())
    al = [int(i) for i in input().split()]
    bi = [i for i in al]
    ans = sum(al)
    for k in range(1, n):
        bi = [min(bi[i-1], al[i]) for i in range(n)]
        ans = min(ans, k * x + sum(bi))
    print(ans)

if __name__=="__main__":
    solve()