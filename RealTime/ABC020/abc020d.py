# 部分点15点はGET

def lcm(a, b, l):
    return (a * b) // gcd(a, b, l)

def gcd(a, b, l):
    if a % b == 0:
        return b

    if l[a % b] > 0:
        return l[a % b]

    tempa = a
    tempb = b
    while a % b != 0:
        temp = b
        b = a % b
        a = temp

    l[tempa % tempb] = b
    return b

N, K = map(int, input().split())
sum = 0
modlist = [0 for _ in range(0, K)]
for i in range(1, N + 1):
    sum += lcm(i, K, modlist)
print(sum % 1000000007)