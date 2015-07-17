# 100point version(viewing slide)
def gcd(a, b, l):
    if a % b == 0:
        l[a] = b
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

modlist = [0 for _ in range(0, K)]
for i in range(0, K):
    gcd(i, K, modlist)

sum = 0
for i in range(1, K + 1):
    M = N - K + i
    num = N // K if N // K > (M - 1) // K else N // K + 1
    As = (K + M) * num // 2 if M % K == 0 else (M % K + M) * num // 2
    gcdsum = (As * K) // modlist[M % K]
    sum += gcdsum

print(sum % 1000000007)