def solve():
	n, k = map(int, input().split())
	al = [int(c) for c in input().split()]
	al.sort()
	ans = 0
	for i in range(k):
		ans += al[i] + i
	print(ans)


if __name__=="__main__":
    solve()
