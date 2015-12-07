N = int(input())
st = [int(input()) for _ in range(N)]
sumscore = sum(st)
table = [[st[i]] for i in range(N)]
knowtable = [[False for i in range(N)] for i in range(N)]
for i in range(int(input())):
    a, b, c = map(int, input().split())
    b, c = b-1, c-1
    if a == 0:
        table[b].append(table[c][0])
        knowtable[b][c] = True
    else:
        if knowtable[b][c]:
            print(table[c][0], table[c][0])
        else:
            knowpeople = N - len(table[b])
            res = sumscore - sum(table[b])
            minscore = max(0, res - (knowpeople - 1) * 100)
            maxscore = 100 if res >= 100 else res
            print(minscore, maxscore)
