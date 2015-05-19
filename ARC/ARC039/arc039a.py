def f(i, x, idx):
    li = list(str(i))
    li[idx] = str(x)
    return int("".join(li))

A, B = map(int, input().split())
clac = lambda s, x, idx: int(str())
amax = max(f(A, 9, 0) - B, f(A, 9, 1) - B, f(A, 9, 2) - B)
bmax = max(A - f(B, 1, 0), A - f(B, 0, 1), A - f(B, 0, 2))
print(max(amax, bmax))
