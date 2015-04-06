N, S = int(input()), input()
slist = [0, 0, 0, 0]
for c in S:
    slist[int(c) - 1] += 1
print(max(slist), min(slist))