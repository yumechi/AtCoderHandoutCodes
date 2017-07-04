def solve():
    total, dowango, niconico = map(int, input().split())
    print(max(0, dowango + niconico - total))

if __name__=="__main__":
    solve()