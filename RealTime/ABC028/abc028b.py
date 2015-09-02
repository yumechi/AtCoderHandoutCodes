li = [0 for _ in range(6)]
for c in input():
	li[ord(c) - ord('A')] += 1
print(" ".join(map(str, li)))
