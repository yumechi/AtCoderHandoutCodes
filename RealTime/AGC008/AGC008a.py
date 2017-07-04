def solve():
    x, y = map(int, input().split())
    print(min(abs(y - x) + (2 if y < x else 0), abs(abs(y + x) + 1)))

if __name__=="__main__":
    solve()