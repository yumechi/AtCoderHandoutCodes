n = int(input())
names = [input() for _ in range(n)]
memos = []
for i in range(n):
    name, t1, t2, impre, t3 = input().split()
    if impre == "good":
        memos.append([name, True])
    else:
        memos.append([name, False])

for i in range(n):
    if not memos[i][1]:
        idx = names.index(memos[i][0])
        memos[idx][1] = not memos[idx][1]

res = []
for i in range(n):
    if memos[i][1]:
        res.append(memos[i][0])

print("\n".join(sorted(res)) if len(res) > 0 else "No answers")
