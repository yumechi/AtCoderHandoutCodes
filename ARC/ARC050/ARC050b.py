def solve():
    red, blue = map(int, input().split())
    needR, needB = map(int, input().split())

    low, high = 0, 10 ** 20
    while high - low > 1:
        mid = (low + high) // 2
        if (red >= mid) and  \
           (blue >= mid) and \
           (red - mid) // (needR - 1) + (blue - mid) // (needB - 1) >= mid:
           low = mid
        else:
           high = mid

    print(low)

if __name__=="__main__":
    solve()