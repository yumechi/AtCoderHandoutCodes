def solve():
    n = int(input())
    al = [int(i) for i in input().split()]
    memos = [0]*n
    for i in range(n):
        memos[i] = i - (al[i] - 1)
    # print(memos)
    ans = 0
    for idx in range(n):
        if memos[idx] == 0:
            if idx != n - 1:
                memos[idx+1], memos[idx] = memos[idx+1]-1, memos[idx]+1
            else:
                memos[idx], memos[idx-1] = memos[idx-1]+1, memos[idx]-1
            ans += 1
        # print(memos)
    print(ans)

if __name__=="__main__":
    solve()
