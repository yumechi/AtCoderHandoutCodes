N = int(input())
s = input()
bottuns = ["A", "B", "X", "Y"]
combos = []

for b1 in bottuns:
    for b2 in bottuns:
        combos.append(b1 + b2)

minnum = 1001
for b1 in combos:
    for b2 in combos:
        if b1 == b2:
            continue
        t = s.replace(b1, "R").replace(b2, "L")
        minnum = min(len(t), minnum)
print(minnum)