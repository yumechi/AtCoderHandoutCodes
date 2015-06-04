N = int(input())
task = sorted([int(input()) for _ in range(3)], reverse=True)
res = 0
for i in range(N):
	N -= task[i%3]
	res += 1
	if N < 1:
		break
print(res)