def solve():
    n, m, k = map(int, input().split())
    for i in range(n + 1):
        selected = m * i
        for j in range(m + 1):
            if selected + (n - i * 2) * j == k:
                print("Yes")
    print("No")

if __name__=="__main__":
    solve()
