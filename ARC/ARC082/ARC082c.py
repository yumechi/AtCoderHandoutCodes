def solve():
    n = int(input())
    al = [int(i) + 1 for i in input().split()]
    amax = max(al) + 3
    ans = [0] * amax
    for i in al:
        ans[i] += 1
        ans[i-1] += 1
        ans[i+1] += 1
    print(max(ans))



if __name__=="__main__":
    solve()
