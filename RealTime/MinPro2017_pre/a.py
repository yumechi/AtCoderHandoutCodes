def solve():
	y, a, h, o = 1, 1, 1, 2
	for c in input():
		if c == "y":
			y -= 1
		if c == "a":
			a -= 1
		if c == "h":
			h -= 1
		if c == "o":
			o -= 1
	print("YES" if y | a | h | o == 0 else "NO")


if __name__=="__main__":
    solve()
