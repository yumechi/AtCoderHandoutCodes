MOD = 10 ** 9 + 7

def gcd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        r = a % b
        a,b = b,r
    return a

def arrgcd(a):
    alen = len(a)
    if alen == 3:
        return gcd(a[0], gcd(a[1], a[2]))
    elif alen == 2:
        return gcd(a[0], a[1])
    elif alen == 1:
        return a[0] # 最初から1つ
    elif alen == 0:
        return 0
    else:
        return gcd(arrgcd(a[:alen//2]), arrgcd(a[alen//2:]))

def solve():
    legnum = int(input())
    legs = [int(input()) for _ in range(legnum)]
    minleg = min(legs)
    gcdval = arrgcd([x - minleg for x in legs if x - minleg > 0])
    print(pow(2, minleg + (gcdval + 1) // 2, MOD))

if __name__=="__main__":
    solve()
