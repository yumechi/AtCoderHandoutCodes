N, R = map(int, input().split())
data = input()

idx, res = 0, 0
last = data.rfind(".")
while N > data.count("o"):
	res += 1
	if data[idx] == "." or idx > last-R:
		next = min(idx+R, N)
		data = data[:idx] + data[idx:next].replace(".", "o") + data[next:]
	else:
		idx += 1
print(res)
