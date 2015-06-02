name = input()
kailength = 0
for i in range(len(name) // 2):
    if name[i] != name[-i-1]:
        kailength += 1
res = 0
if kailength == 1:
    res += 25 * (len(name) - 2) + 24 * 2
else:
    if kailength == 0 and len(name) % 2 == 1:
        res += 25 * (len(name) - 1)
    else:
        res += 25 * len(name)

print(res)
