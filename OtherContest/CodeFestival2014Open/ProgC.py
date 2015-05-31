def calc(num):
    numli = list(map(int, list(str(num))))
    numli = numli[::-1]
    res = 0
    for i in range(0, len(numli)):
        res += numli[i] * (num ** i)
    return res

A = int(input())
if A < 10:
    print(-1)
    exit(0)

res = 1
while True:
    c = calc(res)
    if A == c:
        print(res)
        break
    elif c > A:
        print("-1")
        break
    res += 1

