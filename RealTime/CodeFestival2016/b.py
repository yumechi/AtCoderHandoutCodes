def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(2)
        return
    ans = []
    anssum = 0
    for i in range(1, n):
        ans.append(str(i))
        anssum += i
        if anssum >= n:
            if anssum == n:
                print("\n".join(ans))
            else:
                ans.remove(str(anssum - n))
                print("\n".join(ans))
            return
    print("\n".join(ans))

if __name__=="__main__":
    solve()