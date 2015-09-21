res = 0
l = [input() for _ in range(12)]
for s in l:
    res += 1 if "r" in s else 0
print(res)
