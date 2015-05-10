def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2 * (n + 3) - 3
    else:
        return 2 ** (n + 3) - 3
 
m, n = map(int, input().split())
print(ackerman(m, n))