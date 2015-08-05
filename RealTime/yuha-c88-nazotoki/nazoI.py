n = int(input())
res = ""
memos = []
for _ in range(n):
    line = input()
    for m in memos:
        res += line[m]
    memos = []
    for i in range(n):
        if line[i] in "monica":
            memos.append(i)
print(res)
