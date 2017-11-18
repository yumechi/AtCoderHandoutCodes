l = [2, 1]
for i in range(2, 87):
    l.append(l[i - 2] + l[i - 1])
print(l[int(input())])
