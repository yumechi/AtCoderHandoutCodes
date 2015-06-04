N, Q = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(Q)]
for elem in table:
	a, b, s, t = elem
	if a <= s < t <= b:
		print(0)
	elif s <= a < b <= t:
		print(100 * (t - s - (b - a)))
	elif a <= s < b:
		print(100 * (t - s - (b - s)))
	elif a < t <= b:
		print(100 * (t - s - (t - a)))
	else:
		print(100 * (t - s))