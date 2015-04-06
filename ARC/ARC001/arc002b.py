A, B = map(int, input().split())
res = 0
table = [0, 1, 1, 5, 5, 5, 5, 5, 10, 10, 10]
while A != B:
    if A - B > 9:
        A -= 10
    elif A - B > 0:
        A -= table[A - B]
    elif B - A > 9:
        A += 10
    elif B - A > 0:
        A += table[B - A]
    res += 1
print(res)