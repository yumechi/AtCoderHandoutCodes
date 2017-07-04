def solve():
	n = int(input())
	al = [int(i) for i in input().split()]
	print("YES" if len([i for i in al if i % 2 == 1]) % 2 == 0 else "NO")


if __name__=="__main__":
    solve()
