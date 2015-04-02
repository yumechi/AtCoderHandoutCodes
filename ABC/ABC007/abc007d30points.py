A, B = map(int, input().split())
sum = 0
for i in range(A, B + 1):
	if str(i).find("4") != 1 or str(i).find("9") != 1:
		sum += 1
print(sum)