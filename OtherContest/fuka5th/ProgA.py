while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    xl = list(map(int, input().split()))
    xl.sort()
    print(sum(xl[0:k]))