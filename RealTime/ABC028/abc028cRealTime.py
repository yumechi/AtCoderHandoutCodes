elems = list(map(int, input().split()))
elems.sort()
table  = [[elems[0], 1], [0, 0]]
for i in range(1, 5):
	for j in range(len(table)):
		if table[j][1] < 3:
			table.append([table[j][0] + elems[i], table[j][1] + 1])
li = set([])
for i in range(len(table)):
	if table[i][1] == 3:
		li.update(set([table[i][0]]))
li = list(li)
li.sort(reverse=True)
print(li[2])
