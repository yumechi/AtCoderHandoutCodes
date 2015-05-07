l = list(map(int, list(input())))
res = l[0]
for i in range(1, len(l)):
     res += l[i] if i % 2 == 0 else -l[i]
print(res)