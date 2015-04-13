A, B = map(int, input().split())
tlist = [0 for _ in range(401)]
uru = lambda x: 1 if (x % 400 == 0 or x % 100 != 0) and x % 4 == 0 else 0
for i in range(1, 401):
    tlist[i] = tlist[i - 1] + uru(i)
calc = lambda x,l:x // 400 * l[400] + l[x % 400]
print(calc(B, tlist) - calc(A, tlist) + uru(A))