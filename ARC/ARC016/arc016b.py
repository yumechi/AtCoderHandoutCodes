N = int(input())
table = [False for _ in range(9)]
res = 0
for _ in range(N):
    slist = input()
    for i in range(9):
        c = slist[i]
        if c == "o":
            if table[i] == False:
                res += 1
                table[i] = True
        else:
            table[i] = False
            if c == "x":
                res += 1
print(res)