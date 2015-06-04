import copy
 
words = [word for word in input().split()]
N = int(input())
for _ in range(N):
	ng = input()
	ngl = len(ng)
	for j in range(len(words)):
		if len(words[j]) != ngl:
			continue
		ummatchidx = []
		for i in range(ngl):
			if words[j][i] != ng[i]:
				ummatchidx.append(i)
		check = copy.deepcopy(ummatchidx)
		for i in range(len(ummatchidx)):
			if ng[ummatchidx[i]] == "*":
				check.remove(ummatchidx[i])
		if len(check) == 0:
			words[j] = "*" * len(words[j])
 
print(" ".join(words))